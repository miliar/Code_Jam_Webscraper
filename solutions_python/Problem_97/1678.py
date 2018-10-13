class recycled:
  
  def __init__(self):
    self.f_in = open('recycled.txt')
    self.f_out = open('recycled_out.txt', 'w')
    lines = int(self.f_in.readline())
    #self.d = self.initDict()

    for i in range(lines):
       response = self.process_line()
       
       self.f_out.write("Case #%d: %d\n" % (i+1, response))
	
  def process_line(self):
    line = self.f_in.readline().rstrip()
    line_length=len(line)    
    values = line.split()
    int_values = [0,0]
    int_values[0] = int(values[0])
    int_values[1] = int(values[1])
    outline = ''
    count = 0
	
    for i in range(int_values[0], int_values[1]+1):      
      for j in range(i+1, int_values[1]+1):
        count += self.process_pair(i,j)
      #outline+= self.d[line[i]]      
    
    #print outline
    #self.f_out.write(outline+'\n')
    return count

  def process_pair(self, m,n):
    str_pair = [''] * 2
    str_pair[0] = str(m)
    str_pair[1] = str(n)
    pair_length = len(str_pair[0])
    for i in range(1, pair_length):
      #print str_pair[0], str_pair[0][i:] + str_pair[0][:i]
      if str_pair[1] == (str_pair[0][i:] + str_pair[0][:i]):
        #print str_pair[1],(str_pair[0][i:] + str_pair[0][:i])
        return 1
    return 0
	
if __name__ == "__main__":
   t = recycled()