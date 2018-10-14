import sys


cases = int(raw_input())
for cc in range(cases):
    s,k = raw_input().split()
    s = list(s)
    k = int(k)

    ans = 0
    n = len(s)
    for i in range(n):
        if s[i] == '-':
            if i+k >n:
                ans = -1
                break
            else:
                for j in range(i,i+k):
                    
                    if s[j] == '-':
                        s[j] = '+'
                    else:
                        s[j] ='-'
              #  print"".join(s)
                ans = ans + 1
                
    for i in range(n):
        if s[i] == '-':
            ans = -1
            break

    print "Case #" + str(cc+1) +": " + ("IMPOSSIBLE" if ans == -1 else str(ans))
    
    
