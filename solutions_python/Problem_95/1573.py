d = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}
f = open('test.in','r')
op = open('test.out','w')
numLines = int(f.readline())
for i in range(numLines):
   op.write('Case #')
   op.write(str(i+1))
   op.write(': ')
   line = f.readline()
   line = line.strip()
   for char in line:
       if char != ' ':
          char = d[char]
       op.write(char);
   op.write('\n')

f.close()
op.close()
