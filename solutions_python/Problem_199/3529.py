import sys
sys.stdin = open('A-large.in','r')
sys.stdout = open('output.out','w')

for case in range(1,int(input())+1):
    data=input().split()
    s,k=list(data[0]),int(data[1])
    n=len(s)
    i=flag=count=0
    while i<n:
        if s[i]=='-':
            if i+k>n:
                flag=1
                print('Case #',case,': IMPOSSIBLE',sep='')
                break
            else:
                count+=1
                for j in range(i,i+k):
                    if s[j]=='-':
                        s[j]='+'
                    else:
                        s[j]='-'
        i+=1
    if not flag:
        print('Case #',case,': ',count,sep='')

sys.stdin.close()
sys.stdout.close()
