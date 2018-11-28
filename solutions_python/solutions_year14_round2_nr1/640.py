# -*- coding: utf-8 -*-
f1 = open('repeater.in')
f2 = open('repeater.out', mode = "w")
i = 0
ind = True
for line in f1 :
    i += 1
    line = line[:-1]
    if i == 1 :
        T = int(line)
        S1 = []
        S2 = []
    else:
        if line != '2' :
            if ind :
                S1.append(line)
                ind ^= True
            else :
                S2.append(line)
                ind ^= True

for test in range(T):
    s1 = S1[test]
    s2 = S2[test]
    i = 0
    t = 0
    fl = False
    while i < max(len(s1),len(s2)) :
        if i< len(s1) :
            q1 = s1[i]
        else :
            q1 = str(0)

        if i< len(s2) :
            q2 = s2[i]
        else :
            q2 = str(0)    
        if q1 != q2 :
            if i == 0 :
                fl = True
                break
            t += 1
            if q1 == s1[i-1] :
                s1 = s1[:i]+s1[i+1:]
            elif q2 == s2[i-1] :
                s2 = s2[:i]+s2[i+1:]
            else :
                t -= 1
                fl = True
                break  
        else :
            i += 1                   
    
    if fl :
        str3 = 'Fegla Won'
    else :
        str3 = str(t)     
    st2 = 'Case #' + str(test+1) + ': ' + str3 + "\n"    
    f2.write(st2)

f2.close()
f1.close()  

