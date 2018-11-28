import sys
sys.stdin = open('B-small-attempt0.in','r')
sys.stdout = open('output.out','w')

for case in range(int(input())):
    t=int(input())
    if t<=9:
        print('Case #',case+1,': ',int(t),sep='')
    for no in range(t,8,-1):
        n=str(no)
        l=len(n)
        m=int(n[-1])
        for i in range(l-2,-1,-1):
            if int(n[i])>m:
                break
            m=int(n[i])
        else:
            print('Case #',case+1,': ',int(no),sep='')
            break

sys.stdin.close()
sys.stdout.close()
