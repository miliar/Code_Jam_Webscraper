def should_not_buy(cost,cookies,f,curr_f,x):
    t1=(x-cookies)/(curr_f)
    cookies=cookies-cost
    t2=(x-cookies)/(curr_f+f)
    if t1<t2:
        return (True, t1)
    return (False, t2)
import sys
sys.stdin=open("/home/kshitij/Downloads/B-large.in","r")
sys.stdout=open("/home/kshitij/Downloads/output.out","w")
t=int(raw_input())
for rt in range(t):
    c,f,x=map(float,raw_input().split())
    t=min(c,x)/2.0
    cookies=min(c,x)
    curr_f=2.0
    while cookies<x:
        res = should_not_buy(c,cookies,f,curr_f,x)
        if res[0]:
            t+=res[1]
            break
        else:
            curr_f+=f
            cookies-=c
            c_rem=c-cookies
            x_rem=x-cookies
            t2=min(c_rem,x_rem)/curr_f
            cookies+=min(c_rem,x_rem)
            t+=t2
    print "Case #%s: %.7f"%(rt+1,t)
sys.stdout.close()
