# -*- coding: utf-8 -*-

def listen(lawn):       
    for q in range(N) :
        m = max(lawn[q*M:(q+1)*M])
        for w in range(M):
            if lawn[q*M+w]<m :
                for j in range(N) :
                    if lawn[q*M+w] != lawn[j*M+w] :
                        return 'N'
    return 'Y' 

f1 = open('lawn.in')
f2 = open('lawn.out', mode = "w")
i = 0
answer =[]
for line in f1 :
    i += 1
    line = line[:-1]
    if i==1 :
        T = int(line)
        k = 0
    else :
        if k == 0:
            k = 1
            N = int(line.split()[0])
            M = int(line.split()[1])
            lawn = [0]*N*M
        elif k != 0 :
            k += 1        
            st = line
            n = 0
            for c in st.split() :              
                lawn[(k-2)*M+n] = c
                n += 1
        if k == N+1 :
            k = 0
            answer.append(listen(lawn))

for i in range(T):
    if answer[i] == 'Y' :
        st3 = 'YES' 
    if answer[i] == 'N' :
        st3 = 'NO' 
    st2 = 'Case #' + str(i+1) + ': ' + st3 + "\n"    
    f2.write(st2)

f2.close()
f1.close()            