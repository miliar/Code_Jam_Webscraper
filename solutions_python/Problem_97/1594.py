import os

def create_map(min, max):
   map = {}
   for i in range(min, max+1):
        for j in range(min, max+1):
                if j>i:
                        map[str(i)+','+str(j)]=False
   return map


def crazy_cycle(min, max, map):
   i=min
   while (i<=max):
      map = update_cycle(str(i), map)
      i=i+1
   return map
   
def update_cycle(n, map):
   size = len(n)
   if size>1:
      for i in range(0, size-1):
         head = n[0:size-i-1]
         tail = n[-i-1:]
         new_num = tail+head
         new_num=new_num.lstrip('0')
         if (n!=new_num) and (int(new_num)>int(n)) and (len(n)==len(new_num)) and ((n+','+new_num) in map):
            map[n+','+new_num] = True
            #print '('+n+','+new_num+') => '+ map[n+','+new_num])
   return map
   
def sum_crazy(map):
   sum = 0
   for key in map:
        if (map[key]):
                sum = sum+1
   return sum





data_filename = 'C-small-attempt0.in'
output_filename = 'C-small-attempt0.out'

file_in = open(data_filename, 'r')
read_lines = file_in.readlines()

file_out = open(output_filename, 'w')

result=[]
i = 0
num_map={}

total_test_line = int(read_lines[i])
i=i+1
for j in range(0, total_test_line):
   (min, max) = read_lines[i].rstrip('\n').split(' ')
   num_map = create_map(int(min), int(max))
   crazy_map=crazy_cycle(int(min), int(max), num_map)
   no_of_cycle=sum_crazy(crazy_map)
   result.append('Case #'+str(j+1)+': '+str(no_of_cycle)+'\n')
   print "-----------------------------------------------------------"
   i=i+1
   
file_out.writelines(result)
file_out.close()
file_in.close()



print 'Result is ', result

print "DONE!!"
