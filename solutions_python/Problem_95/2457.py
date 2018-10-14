#read input
inputfile = open('A-small-attempt1.in')
#define mapping lists ...
s =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

g =['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q',' ']
lines = inputfile.readlines()
inputfile.close()
cases = int(lines[0])
count = 1
output = ''
while(count <= cases):
   Gsentence = lines[count]
   Ssentence = ''
   for character in Gsentence:
      if character != '\n':
         Ssentence += s[g.index(character)]
   print'Case #%d: %s' % (count,Ssentence)
   output += 'Case #%d: %s\n' % (count,Ssentence)
   count += 1
outputfile = open('output','w')
outputfile.write(output)
outputfile.close()
#end prog ...
#codejam 2012 problem A ...
