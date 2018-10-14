import math

def isPali(a):
    ra = str(a)[::-1]
    return str(a) == ra

input = open('C-small-attempt0.in','r')
n = int(input.readline())
ret = ''
t = 0
while t < n:
    (a,b) = input.readline().split()
    a = math.sqrt(int(a)); b = math.sqrt(int(b))
    c = 0
    i = int(math.ceil(a))
    while i <= b:
        s = int(i**2)
        if isPali(i) and isPali(s):
            #print i,s
            c += 1
        i += 1
    ret += 'Case #'+str(t+1)+': '+str(c)+'\n'
    t += 1

output = open('output.txt', 'w')
output.write(ret)
output.close()
