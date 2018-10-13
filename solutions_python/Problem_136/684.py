import sys
buf=[]
def scans():
    global buf
    while 1:
        while len(buf) <= 0:
            buf=input().replace('\n',' ').split(' ')
        o=buf.pop(0)
        if o!='':
            break
    return o
def scan():
    return int(scans())
def scanf():
    return float(scans())

sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')
for t in range(1,1+scan()):
    c,f,x = scanf(),scanf(),scanf()
    btm = 0
    n = 0
    last = x/2
    while 1:
        btm += c/(2+n*f)
        n+=1
        nw = btm+x/(2+n*f)
        if nw>last:
            break
        else:
            last=nw
    print("Case #%d: %.7f"%(t,last))