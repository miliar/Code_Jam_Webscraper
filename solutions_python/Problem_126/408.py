import re
import math

lines = open('A-small-attempt0.in').read().splitlines()

num_cases = int(lines[0])

output = []

def substr(string):
    j=1
    a=[]
    while True:
        for i in range(len(string)-j+1):
            a.append(string[i:i+j])
        if j==len(string):
            break
        j+=1
        #string=string[1:]
    return a


def isValid(l, n):
    for s in l:
        if len(s) >= n:
            return True
    return False


def nValue(word, n):
    count = 0
    for s in substr(word):
        l = re.split(r'[aeiou]',s)
        if isValid(l, n):
            count += 1
    return count


for i in range(num_cases):
    start = i + 1
    word, n = lines[start].split(' ')
    ret = str(nValue(word,int(n)))
    print ret
    output.append(ret)

o_file = open('A-small-attempt0.out', 'w+')
for i in range(num_cases):
    o_file.write("Case #%s: %s\n" % ( str(i+1), output[i] ))