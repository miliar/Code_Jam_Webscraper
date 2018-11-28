f = file("test.in",'r')
lines = f.readlines()
f.close()

t = int(lines[0])

for i in range(1,t+1) :
    n = int(lines[i].split(' ')[0])
    s = int(lines[i].split(' ')[1])
    p = int(lines[i].split(' ')[2])
    #print n,s,p
    count = 0
    totalscores = []
    for j in range(3,n+3) :
        totalscores.append(int(lines[i].split(' ')[j]))
    for j in range(0,n) :
        total = totalscores[j]
        if total == 0:
           if p == 0 :
              count+=1
              continue
           else :
                continue
        minscore = total/3
        if minscore >= p :
           count+=1
        elif p-minscore == 1 :
             if total%3 != 0 :
                count+=1
             else:
                  if s > 0 :
                     count+=1
                     s=s-1

        elif p-minscore == 2 :
             if total%3 == 2 :
                if s > 0 :
                   count+=1
                   s=s-1
    #print "Case #"+str(i)+": "+str(s)
    print "Case #"+str(i)+": "+str(count)


