def cons(s,m):
    n=len(s)
    for i in range(n-m+1):
        count =0
        for j in range(m):
              if(s[i+j]!='a' and s[i+j]!='e' and s[i+j]!='i' and s[i+j]!='o' and s[i+j]!='u'):
                count=count+1
              else:
                  break         
              if(count==m):
                return 1
    return 0

inp = open('input.in','r')
out = open('output.txt','w')
x=[x for x in inp.readline().split()]
T=int(x[0])
for i in range(T):
    x=[x for x in inp.readline().split()]
    string = x[0]
    lent=int(x[1])
    n=len(string)
    lst=[]
    for j in range(n):
        for k in range(j+lent-1,n):
            lst.append(string[j:k+1])
    s=len(lst)
    ret=0;
    for k in range(s):
        print
        if(cons(lst[k],lent)):
            ret=ret+1
    out.write('Case #')
    out.write(str(i+1))
    out.write(': ')
    out.write(str (ret))
    out.write('\n')
    
