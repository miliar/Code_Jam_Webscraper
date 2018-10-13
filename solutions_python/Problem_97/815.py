

def run():
    f=open("input.in")
    g=open("out.txt",'w')
    num = int(f.readline())
    for i in range(num):
        g.write("Case #%d: " % (i+1))
        [A,B] = map(int, f.readline().split())
        total=0
        for x in range(A,B):
            total+=brute(x,A,B)
        g.write("%d\n" % total)
        continue
    f.close()
    g.close()

def digits(n):
    return len(str(n))

def cycle(n,k):
    temp = str(n)
    return int(temp[-k:] +temp[:-k])

def brute(trial, A, B):
    count = 0
    res = [cycle(trial,i) for i in range(1,digits(trial))]
    for cur in res:
        if cur>trial and cur<=B and digits(cur)==digits(trial):
            count=count+0.0+1.0/res.count(cur)
    return count
    
