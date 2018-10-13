

t = int(input())

def validate(n):
    prev =None
    for k in str(n):
        if prev != None and prev>int(k):
            return False
        prev = int(k)
    return True
for k in range(t):
    n = int(input())
    nn = n
    while not validate(n):
        n-=1
    print("Case #%d: %s"%(k+1,n))