def decrease(s):
    #print('dec',s)
    if not s: import pdb;pdb.set_trace()
    return str(int(s)-1).lstrip('0')

def solve(s):
    if len(s)==1 : return s

    last=s[0]
    flag=False
    for i,digit in enumerate(s[1:],1):
        if digit<last:
            flag=True
            break

        last=digit

    if not flag: return s

    return decrease(s[:i])+'9'*len(s[i:])

def doit(s):
    last=s
    now=solve(last)

    while last!=now:
        #print(last,now)
        last=now
        now=solve(last)

    return now

K=int(input())

for i in range(K):
    print('Case #{}: {}'.format(i+1,doit(input())))
    

