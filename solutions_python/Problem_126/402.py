def judge(name, n):
    for i in range(len(name)-n+1):
        s= name[i:i+n]
        if 'a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s:
            continue
        else:
            return True
    return False
    
def batch(name, n):
    res=0
    for i in range(len(name)):
        for j in range(i+n, len(name)+1):
            sub=name[i:j]
            if judge(sub, n):
                res+=1
    return res
    
filename= "A-small-attempt0.in"
f= open(filename)
num_cases = int(f.readline())
for casenum in range(1, num_cases+1):
    elem = f.readline().split()
    name = elem[0]
    num = int(elem[1])
    res=batch(name, num)
    print "Case #%d: %d" % (casenum, res)
