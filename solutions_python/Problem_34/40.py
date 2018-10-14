import re
import os


ifilename = r'D:\A-large.in'
ofilename = r'D:\A-large.out'


ifile = open(ifilename, 'r')
input = ifile.readlines()
ifile.close()

param = map(int, input[0].split())

L = param[0]
D = param[1]
N = param[2]

adict = input[1:1+D]
test = input[1+D:]


def convert(s):
    result = ""
    inp = False
    for i in range(len(s)):
        if s[i] == '(':
            inp = True
        if s[i] == ')':
            result = result[:-1]
            inp = False
        result = result + s[i]
        if inp and s[i] <> '(':
            result = result + '|'


    return result

test = map(convert, test)

result = []

for i in range(N):
    print i
    s = test[i]
    pattern = re.compile(s)
    count = 0
    for word in adict:
        if pattern.match(word):
            count += 1
    result.append(count)

ofile = open(ofilename, 'w')
for i in range(N):
    line = 'Case #' + str(i+1) + ': ' + str(result[i]) + '\n'
    ofile.write(line)

ofile.close()
    
    
        
        
        
