def flipper(s):
        i=0
        while i< len(s)-1:
                if int(s[i])> int(s[i+1]):
                        break
                i+=1
        if i== len(s)-1:
                return s
        x= [y for y in s]
        while i>=1 and x[i]== x[i-1]:
                i-=1
        for j in range(i+1, len(s)):
                x[j]='9'
        x[i]= str(int(x[i])-1)
        if x[0]=='0':
                return ''.join(x[1:])
        return ''.join(x)

t= int(input())
for i in range(1, t+1):
        s= input()
        if len(s)==1:
                print('Case #{}: {}'.format(i, s))
                continue
        print('Case #{}: {}'.format(i, flipper(s)))