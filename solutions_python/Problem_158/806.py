f1 = open('omni.in')
f2 = open('omni.out', mode = "w")
i = 0
for line in f1 :
    i += 1
    line = line[:-1]
    if i == 1 :
        T = int(line)
        X = []
        R = []
        C = []
    else:
        l = line.split()
        X.append(int(l[0]))
        R.append(int(l[1]))
        C.append(int(l[2]))

res = []

for i in xrange(T) :
    if R[i]*C[i] % X[i] == 0 and min(R[i],C[i]) > X[i]-2 :
        res.append('GABRIEL')
    else :
        res.append('RICHARD')

for i in range(T):
    st = 'Case #' + str(i+1) + ': ' + res[i] + "\n"    
    f2.write(st)

f2.close()
f1.close()