import sys

#sys.stdin = open("in.txt")
sys.stdin = open("C:\\Users\\Kuldeep\\Downloads\\C-small-attempt0.in")
sys.stdout = open("C:\\Users\\Kuldeep\\Desktop\\out.txt",'w')

t = int(raw_input())

for tc in range(1,t+1):
    n , l , h = map(int, raw_input().split())
    p = map(int, raw_input().split())
    flag = 0
    ans = -1
    for i in range(l,h+1):
        flag = 0
        for j in range(n):
            if p[j]%i!=0 and i%p[j]!=0:
                flag = 1
                break
        if flag==0:
            ans = i
            break
    
    sys.stdout.write("Case #"+str(tc)+": ")
    if ans>0:
        print ans
    else:
        print 'NO'