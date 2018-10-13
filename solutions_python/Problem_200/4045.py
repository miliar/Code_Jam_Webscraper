# Enter your code here. Read input from STDIN. Print output to STDOUT
def sumtototal(total, coins_list,cnt,i):
    if total==0 and i<len(coins_list):
        return cnt
    else:
        t1=sumtototal(total,coins_list,cnt,i+1)
        t2=sumtototal(total-coins_list[i],coins_list,cnt+1,i+1)
        if t1<t2:
            return t1
        else:
            return t2
for i in range(int(raw_input())):
    wt=int(raw_input())
    n=int(raw_input())
    arr=map(int,raw_input().split())
    print sumtototal(wt,arr,0,0)
