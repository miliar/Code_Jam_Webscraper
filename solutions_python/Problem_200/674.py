import math
import time

start = time.time()
num = int(input())

i = 1


while i <= num:
    g = time.time()
    line = input()
    #line = fd.readline()
    #print(line)
    length = len(line)
    ans = ''
    if len == 1:
        ans = line
    else:
        same = 0
        for j in range(length):
            kk = int(line[j])
            if j > 0 and line[j] != line[j-1]:
                same = j
            if j < (length-1):
                
                if kk > int(line[j+1]):
                    
                    d = '9' * (length-1-same)
                    ans = ans[:same]
                    ans+= str(kk-1)
                    ans += d
                    break
                
                    
            
            ans += line[j]
        k = None
        for g in range(length):
            if ans[g] == '0':
                k = g
            else:
                break
        if k != None:
            ans = ans[k+1:]
    s = 'Case #' + str(i) + ': ' + ans 
    print(s)
    
    i += 1
    

#print(time.time()-start)

