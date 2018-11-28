import sys

r = open('A-large.in.txt','r')
f = open('outputnewlarge.txt','w')
##sys.stdin = r
##sys.stdout = f
k = -1 
for i in r:
    if k == -1:
        a = int(k)
        k = 0
        continue
    l = i
    b = l.split()
    ##print b 
    sum = 0
    ppl = 0
    for j in range(int(b[0])+1):
        if sum < j:
            ppl += j-sum
            sum = j
        sum += int(b[1][j])
    k+=1
    st = "Case #" + str(k) +": " + str(ppl) + '\n'
    f.write(st)
f.close()
            
        
    
