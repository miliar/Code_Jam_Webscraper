memo={}
def istidy(n):
    s=str(n)
    for i in range(1,len(s)):
        if s[i]< s[i-1]:
            return False
    return True

n=1000
last=0
for i in range(1,1000+1):
    if istidy(i):
        last=i
    memo[i]=last
'''
for i in memo.keys():
    print(i,memo[i])

'''

t=int(input())
for x in range(1,t+1):
    n=int(input())
    print('Case #%d: %d'%(x,memo[n]))
