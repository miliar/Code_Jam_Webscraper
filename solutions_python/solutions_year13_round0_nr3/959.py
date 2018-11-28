'''
Created on Apr 12, 2013

@author: Phil
'''
import math

def ispalindrome(x):
    s = str(x)
    e = len(s)-1
    for i in range(int(e/2)+1):
        if s[i]!=s[e-i]:
            return False
    return True
    

fname = input('In file: ')
namefile = fname.split('.')[0]

fr = open(fname, 'r')
fc = fr.read()
fr.close()

lines = fc.split('\n')
output = ""
numCases = int(lines[0])

for n in range(numCases):
    A = int(lines[n+1].split(' ')[0])
    B = int(lines[n+1].split(' ')[1])
    i = math.ceil(math.sqrt(A))
    c = 0;
    while i*i<=B:
        if ispalindrome(i) and ispalindrome(i*i):
            c+=1
        i+=1
    output += "Case #"+str(n+1)+": "+str(c)+"\n"


output=output[:-1]
fw = open(namefile+'.out', 'w')
fw.write(output)
fw.close()