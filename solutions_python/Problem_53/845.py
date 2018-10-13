import array

f = open('A-OUT-BIG','w')
inp = open ("A-large.IN")
#read line into array
n = int(inp.readline().split()[0])
print n
k=0
for line in inp.readlines():
    k+=1
    pair = (map(int, line.split()))
    if (pair[1]+1)%(2**pair[0]) == 0:
        f.write("Case #"+ str(k) + ": ON\n")
        #print "Case #"+ str(k) + ": ON\n"
    else:
        f.write("Case #"+ str(k) + ": OFF\n")
        #print "Case #"+ str(k) + ": OFF\n"
f.close()
inp.close()
