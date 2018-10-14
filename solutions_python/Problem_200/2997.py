t = input()
import copy
def issorted(s):
    f = 0
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            f = 1
            break
    if f == 1:
        return 0
    else:
        return 1
for i in range(t):
    n = list(raw_input())
    m = copy.copy(n)
    while issorted(n) == 0:
        for j in range(len(n)-1):
            if n[j] <= n[j+1]:
                continue
            else:
                
                while n[j] > n[j+1]:
                    if n[j+1] != '9':
                        n[j+1] = '9'
                    if m < n:
                        n[j] = str(int(n[j]) - 1)
                
    print 'Case #' + str(i+1) + ': ' + str(int(''.join(n)))
       
