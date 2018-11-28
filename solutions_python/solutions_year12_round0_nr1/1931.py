import sys

"""
N = int(sys.stdin.readline().strip())
for qw in range(1, N+1):
  print 'Case #%d:' % qw,

  num = sys.stdin.readline().strip()
  values = {num[0]: 1} #{num[0]: 1} can be hash
  for c in num:
    if c not in values:
      sz = len(values)
      if sz == 1:
        values[c] = 0
      else:
        values[c] = sz
  result = 0
  base = max(len(values), 2)
  for c in num:
    result *= base
    result += values[c]
  print result
"""

'''
infile = file("test.txt", 'r')
count = 0
plaDict = {}
for line in infile :
        print "line : "+line
        line = line.lstrip('\n')
        if count == 0:
                lcase = line.split()
        else :
                List = line.split('-')
                print "List : "
                print List
                for pla in range (len(List[0])) :
                        plaDict[List[0][pla]] = List[1][pla]
        count = count + 1
print plaDict


#http://www.daniweb.com/software-development/python/threads/33588/ways-to-create-dictionary

        
'''

infile = file("A-small-attempt1.in",'r')
count = 0
LastString = ''
plaDict = {'q': 'z', 'z': 'q', '\n': '', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}

for line in infile :
        PP = ''
        sentence = ''
        line = line.lstrip('\n')
        #print line
        if count == 0:
                lcase = int(line.lstrip(' '))
        else :
                for i in range (len(line)) :
                        #print plaDict[line[i]]
                        Letter =  plaDict[line[i]]
                        #print "Letter : "+Letter
                        sentence = sentence + Letter #print "Sen : "+sentence
                        PP = "Case #"+str(count)+": "+sentence
                #LastString = "Case #"+str(count)+": "+sentence
                #print LastString
        if 0 < count < lcase :
                LastString = LastString + PP + '\n'
        elif count == lcase :
                LastString = LastString + PP

        count = count + 1
print LastString

fo = open("P1.out", "w")
fo.write(LastString);
#close opend file
fo.close()

