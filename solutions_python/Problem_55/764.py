#!/usr/bin/python

class ThemePark:
  def __init__(self):
    self.outfile = open('third_other.out','w')
    self.infile = open('C-large.in','r')
    print "start"
    
  def __del__(self):
    self.outfile.close()
    self.infile.close()
    print "end"
    
  def set_first_line_read(self, line):
    split_str = line.split(" ")
    self.day_run = int(split_str[0])
    self.people_limit = int(split_str[1])
    self.max_group_index = int(split_str[2])
    
  def set_second_line_read(self, line):
    list = line.split(" ")
    self.group_list = map(lambda x:int(x), list)
    
  def set_group_iter(self):
    people = 0
    group_index = 0
    first_group_index = 0
    tmp_list = []
    while True:
      tmp_list.append(group_index)
      people += self.group_list[group_index]
      next_group_index = self.get_next_group_index(group_index)
      if (first_group_index == next_group_index) or (people + self.group_list[next_group_index] > self.people_limit):
        if self.group_unique.count(tmp_list) != 0:
          self.unique_start_index = self.group_unique.index(tmp_list)
          self.unique_length = len(self.group_unique) - self.unique_start_index
          break
        self.group_unique.append(tmp_list)
        self.group_unique_sum.append(people)
        tmp_list = []
        people = 0
        first_group_index = next_group_index
      group_index = next_group_index
    
  def process_init(self):
    self.group_unique = []
    self.group_unique_sum = []
    self.unique_start_index = -1
    self.unique_length = -1
        
  def process(self):
    self.process_init()
    test_time = 1
    for time, line in enumerate(self.infile):
      if time == 0:
        continue
      if time%2 == 1:
        self.set_first_line_read(line.strip())
        continue
      self.set_second_line_read(line.strip())
      self.set_group_iter()
      """
      print self.group_unique
      print self.group_unique_sum
      print self.unique_start_index
      print self.unique_length
      """
      self.print_result(test_time, self.get_money())
      self.process_init()
      test_time += 1
          
  def get_money(self):
    if self.unique_length == 1:
      return self.day_run * sum(self.group_unique_sum)
    non_unique_list = self.group_unique_sum[:self.unique_start_index]
    money = sum(non_unique_list)
    x_times = (self.day_run - len(self.group_unique_sum[:self.unique_start_index])) / self.unique_length
    money += x_times * sum(self.group_unique_sum[self.unique_start_index:self.unique_start_index+self.unique_length])
    x_mod = (self.day_run - len(non_unique_list)) % self.unique_length
    money += sum(self.group_unique_sum[self.unique_start_index:self.unique_start_index + x_mod])
    return money
    
  def get_next_group_index(self, current_group_index):
    if current_group_index + 1 >= self.max_group_index:
      return 0 
    return current_group_index + 1
    
  def print_result(self, time, money):
    result_str = "Case #%(time)s: %(money)s\n" % {'time':time, 'money':money}
    self.outfile.write(result_str)

a = ThemePark()
a.process()
