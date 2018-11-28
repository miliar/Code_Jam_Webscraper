def isOk((a,b)):
    for i in range(1,len(a)+1):
        if b == (a[i:]+a[:i]):
            return True
    return False

def recycled(a,b):
    list = [elem for l1 in [[(str(i),str(j)) for j in range(i+1,b+1)] for i in range(a,b+1)] for elem in l1]
    i = 0
    for p in list:
        if isOk(p):
            i=i+1
    return i

nb = int(raw_input())
response = {}
for i in range(1,nb+1):
    l = raw_input().split()
    a = int(l[0])
    b = int(l[1])
    response[i] = recycled(a,b)
for a,b in response.items():
    print "Case #"+str(a)+": "+str(b)
