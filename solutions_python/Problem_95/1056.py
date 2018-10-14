import math
def plusn(a,n):
    newn=n
    position = ord(a)
    if position+n>122:
        position=96
        n=122-(position+n)
    if position==122:
        position=96
    if n>26:
        times=math.floor(n/26)
        newn=int(n-26*times)
    return chr(position+newn)
f=open('input.txt','r')
data=f.readlines()
print data
for line in data:
    for char in line:
        char=plusn(char,10)
        print char
print data
