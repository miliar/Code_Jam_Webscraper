import sys

f = open("A-large.in",'r')
out = open("out.txt","w")

t = f.readline()
for it in range(int(t)):
    line = f.readline().strip('\n').split(' ')
    n = int(line[0])
    c = line[1]
    #L = f.readline().strip('\n').split(' ')
    #L = map(int,f.readline().strip('\n').split(' '))
    L = map(int,c)

    ans = 0
    for i in range(len(L)):
        if i > 0:
            summ = reduce(lambda x,y:x+y, L[:i])
            while summ + ans < i:
                ans = ans+1
    
    #x = func(L, c)
    
    out.write("Case #"+str(it+1)+": " + str(ans) + "\n")
                
    
f.close()
out.close()
