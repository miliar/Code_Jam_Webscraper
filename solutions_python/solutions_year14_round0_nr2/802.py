# -*- coding: utf-8 -*-
f1 = open('cookie.in')
f2 = open('cookie.out', mode = "w")
i = 0
for line in f1 :
    i += 1
    line = line[:-1]
    if i == 1 :
        T = int(line)
        C = []
        F = []
        X = []
    else:
        l = line.split(" ")
        C.append(float(l[0]))
        F.append(float(l[1]))
        X.append(float(l[2]))

for i in range(T):
    time = 0
    current_rate = 2
    while(X[i]/current_rate > (C[i]/current_rate+X[i]/(current_rate+F[i]))) :
        time += C[i]/current_rate
        current_rate += F[i]
    time += X[i]/current_rate
    time+= 0.00000005       
    st2 = 'Case #' + str(i+1) + ': ' + str(time) + "\n"    
    f2.write(st2)

f2.close()
f1.close()  