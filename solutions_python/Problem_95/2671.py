sample = """
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
"""

sol = """
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
"""
mapping = {'q':'z', 'z': 'q'}
for index in range(len(sample)):
  mapping[sample[index]] = sol[index]

#mapping done translate it now
problem = open("A-small-attempt1.in", 'r').read()
result = open("sol_a.out", 'w')
line_num = 1
lines =  problem.split('\n')
num_lines = int(lines[0])
for index in range(1,num_lines+1 ):
  new_line = "Case #%d: " %line_num
  line_num += 1
  for char in lines[index]:
    new_line += mapping[char]
  result.write(new_line+ '\n')
result.close()
