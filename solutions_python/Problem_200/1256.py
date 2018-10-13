t = int(input())

for r in range(t):
        s = list(map(int,list(input())))
        print ("Case #",r+1,':',sep='',end = ' ')
        l = len(s)
        for n in range(1,l):
                if s[n] < s[n-1] :
                        for m in range(n,l):
                                s[m] = 9
                        s[n-1] = s[n-1]-1
                        
                        for m in range (n-1,-1,-1):
                                if s[m] > s[m+1]:
                                        s[m] = s[m] - 1
                                        s[m+1] = 9
                                          
        if s[0] == 0:
                s = s[1:]
                l = l-1
        for n in range(l):
                if s[n] == 0:
                        s[n] = 9
                print(s[n],end = '')
        print()                        
