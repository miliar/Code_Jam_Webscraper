t = int(input()) 
l = [int(input()) for i in range(t)]

def calc(x):
    def is_tidy(x):
       s=str(x)
       l=len(s)
       ilast = int(s[-1])
       for i,el in enumerate(reversed(s[:-1])):
           m = int(el)
#           print(i,l-i+1)
           if m>ilast: return l-i-1
           ilast=m
       return -1
    while x>0:
       index = is_tidy(x)
       if index==-1: 
           return x
       x -= int(str(x)[index:])+1

for i in range(t):
    print ('Case #{}: {}'.format(i+1,calc(l[i])))
