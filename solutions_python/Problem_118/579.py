import math
def palindrome(s):
    if(len(s)==0 or len(s)==1):
        return 1
    elif(s[0]==s[-1]):
        return palindrome(s[1:-1])
    else:
        return 0
def incr(s):
    if(len(s)==1):
        return str(int(s)+1)
    if(len(s)%2==0):
        d,c=(s[:int(len(s)/2)]),s[int(len(s)/2):]
        temp=int(d[::-1])
        tmp=d
        if(temp<=int(c) and len(str(int(tmp)+1))==len(tmp)):
            st=str(int(tmp)+1)
            return st+st[::-1]
        elif(temp==int(c) and len(str(int(tmp)+1))>len(tmp)):
            st=str(int(tmp)+1)
            tmp=st[:-1]
            return st+tmp[::-1]
        elif(temp>int(c)):
            st=str(tmp)
            return st+st[::-1]
    else:
        d,c=(s[:int(len(s)/2)]),s[int(len(s)/2)+1:]
        mid=s[int(len(s)/2)]
        temp=int(d[::-1])
        tmp=(s[:int(len(s)/2)+1])
        if(temp<=int(c) and len(str(int(tmp)+1))==len(tmp)):
            st=str(int(tmp)+1);
            mid=st[-1]
            st=st[:-1]
            return st+mid+st[::-1]
        elif(temp==int(c) and len(str(int(tmp)+1))>len(tmp)):
            st=str(int(tmp)+1)
            tmp=st[:-2]
            return st+tmp[::-1]
        elif(temp>int(c)):
            st=str(tmp)
            st=st[:-1]
            return st+mid+st[::-1]
                    
inp = open('input.in','r')
out = open('output.out','w')
nn = [int(x) for x in inp.readline().split()]
for j in range(nn[0]):
    c=0
    a, b = [int(x) for x in inp.readline().split()]
    #print(' ',a,' ',b, ' ')
    m,n=math.ceil(math.sqrt(a)), int(math.sqrt(b))+1
    ##print(' ',m,' ',n, ' ')
    s=str(m)
    sq=int(s)
    while(sq*sq<=b):
        #print(s)
        if(palindrome(str(sq*sq))==1 and sq*sq<=b):
            #print(s)
            c=c+1
        s=incr(s);
        sq=int(s)
    #print('\n',c,'\n')
    out.write('Case #')
    out.write(str(j+1))
    out.write(': ')
    out.write(str (c))
    out.write('\n')
