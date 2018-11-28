def formatter(index,val):
    print('Case #{0}: {1}'.format(index,val))

def solve(c,f,x):
    if x<=2.0:
        return (x/2.0)
    prev_c = 0
    prev_x = x
    j=2.0
    while(True):
        cur_c = (c/j) + prev_c
        cur_x = (x/j) + prev_c
        if cur_x > prev_x:
            return prev_x
        prev_x = cur_x
        prev_c = cur_c
        j+=f


t = int(input())
for tc in range(t):
    c,f,x = map(float,input().split())
    formatter(tc+1,solve(c,f,x))

        


