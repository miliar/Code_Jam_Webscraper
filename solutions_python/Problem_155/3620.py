
def spec(d):
    aud = sum(d)
    count = 0 #citi deja aplauda
    necesary = 0 # citi vor fi nevoie
    for i in range(len(d)):
        if d[i]>0 and i<= (count+necesary):
            count+=d[i]
        elif d[i]>0 and i>(count+necesary):
            necesary+=(i-count-necesary)
            count+=d[i]
            print i, count, necesary, d[i]
    return necesary
        

f = open('small.input', 'r')
T = int(f.readline())
p=[] #people
print T, "testcases"

for i in range(T):
    l = f.readline()
    k = int(l[0])
    d=[]
    for j in range(k+1):
        d.append(int(l[j+2]))
    p.append(d)
# data is readed
f.close()
f = open('smalloutput.txt', 'w')
for i in range(T):
    f.write("Case #%s: %s\n" % (i+1, spec(p[i])))
