import re
f = open('A-large.in')
h = 0
count = 1
for line in f:
    if h!=0:
        ppl = 0
        need = 0
        data = re.split('\s', line)
        string = str(data[1])
        limit = int(data[0])+1
        for x in range(0,limit,1):
            if x==0:
                ppl+=int(string[x])
            else:
                if int(string[x])!=0:
                    if ppl<x:
                        temp = x-ppl
                        need += temp
                        ppl+=int(string[x])
                        ppl+=temp
                    else:
                        ppl+=int(string[x])
        print "Case #%d: %d" % (count,need)
        count+=1
    else:
        h+=1

f.close()