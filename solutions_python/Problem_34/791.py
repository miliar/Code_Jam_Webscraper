#!/usr/bin/python
import sys, time

def parse(case):
    words = []
    if len(case) <= 1:
        return case
    else:
        for letter in case[0]:
            for suffix in parse(case[1:]):
                if type(suffix) == list:
                    for s in suffix:
                        word = letter + str(s)
                        words.append(word)
                else:
                    word = letter + str(suffix)
                    words.append(word)
        return words
        
def test(cases):
    global dct
    global L
    correct = []
    output = []
    for i in range(len(cases)):
        correct.append(0)
        case = cases[i]
        #print 'case', case
        for word in dct:
            #print 'word', word
            for j in range(int(L)):
                if word[j] in case[j]:
                    #print word[i], "in", case[j]
                    if j == int(L) -1:
                        correct[i] += 1
                    continue
                else:
                    break
    for x in range(len(correct)):      
        y = x + 1
        output.append('Case #' + str(y) + ': ' + str(correct[x]))
    return output
    
if len(sys.argv) < 2:
  exit()
infile = sys.argv[1]
try:
  f = open(infile, 'r')
except IOerror:
  print "File open error"
  exit()
  
#read L D N
(L, D, N) = f.readline().split(' ')

#Gen word list
dct = []
for i in range(int(D)):
  dct.append(f.readline().strip())

#Gen each case
cases = []
for i in range(int(N)):
    line = f.readline()
    case = []
    group = False
    for x in line[:-1]:
        if x == '(':
            group = True
            curr = []
        elif x == ')':
            case.append(curr)
            group = False          
        else:
            if group:
                curr.append(x)
            else:
                case.append(x)
    cases.append(case)
      
#parse each case
output = test(cases)
'''output = []
for i in range(len(cases)):
    time1 = time.time()
    words = parse(cases[i])
    time2 = time.time()
	print "case", i, "took ", time2 - time1
	#print words
    count = 0
    for word in words:
        if word in dct:
            count += 1
    output.append('Case #' + str(i) +': ' + str(count))'''

outfile = open('output.out', 'w')
for line in output:
    outfile.write(line + '\n')
