f = open('B-small-attempt0.in','r')
o = open('output.txt','w')
n = eval(f.readline())

for i in range(n):
    line = f.readline().replace('\n','')
    # print(line)
    tidynum = str(line)

    if(len(line)>1):
        tidynum = ""

        
        a = [0,0]
        for c in range(len(line)-1):
            
            int1 = int(line[c])
            int2 = int(line[c+1])

            if(int1 == int2):
                if(not equal):
                    a  = [c,0]
                    equal = True
                a[1] +=1
            else:
                equal = False 
            
            if(int1 <= int2):
                tidynum += str(int1)
                if(c == len(line)-2):
                    tidynum += str(int2)
                continue
            
               
            
            
            if(int1 > int2):
                # print(a)
                if(a[1] > 0):
                    temp = tidynum[0:a[0]]
                    temp += str(int1 - 1)
                    
                    temp += '9'*(len(line)-a[0]-1)
                    
                    tidynum = temp
                else:
                    tidynum += str(int1-1)
                    tidynum += '9'*(len(line)-c-1)
    
                break
            
            
        tidynum = str(int(tidynum))
    # print(tidynum)
    o.write('Case #%d: %s'%(i+1,tidynum))
    if(i < n-1):
        o.write('\n')
f.close()
o.close()


# 13332
# 12999
# 
# 1+2+999