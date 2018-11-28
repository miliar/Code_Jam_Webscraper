import os,sys
f = open('./input.txt',"r")
output = open('./output.txt',"w")
def out(t,sol):
    s = "Case #" + str(t+1) + ": " + str(sol)
    print(s)
    output.write(s + "\n")
T = int(f.readline())
def read():
    return f.readline()[:-1]

def deal(n):
    if len(n) == 1:
        return n
    a = n[0]
    m = a*len(n)
    if n>=m:
        return a + deal(n[1:])
    x = '9'*(len(n)-1)
    if a != '1':
        x = str(int(a)-1) + x
    return x

for t in range(0,T):
    N = read()
    x=deal(N)
    out(t, x)
output.close()