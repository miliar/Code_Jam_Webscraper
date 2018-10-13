# -*- coding: utf-8 -*-
f1 = open('trick.in')
f2 = open('trick.out', mode = "w")
i = 0
first_answer = True
matrix_row = 0
Answer = []
for line in f1 :
    i += 1
    line = line[:-1]
    if i == 1 :
        T = int(line)
        M1 = []
        M2 = []
    else:
        l = line.split(" ")
        if len(l) == 1 :
            if first_answer :
                fa = int(l[0])
            else:
                sa = int(l[0])
            first_answer ^= True           
        else:
            matrix_row += 1
            if matrix_row == 5 :
                matrix_row = 1
            if not first_answer :
                if matrix_row == fa :
                    for numbers in l :
                        M1.append(numbers)
            if first_answer :
                if matrix_row == sa :
                    for numbers in l :
                        M2.append(numbers)
                    Answer.append(set(M1).intersection(M2))
                    M1 = []
                    M2 = []

for i in range(len(Answer)):
    k = len(Answer[i])
    ans = ''
    if k == 0 :
        ans = 'Volunteer cheated!'
    if k == 1 :
        ans = Answer[i].pop()
    if k > 1  :
        ans = 'Bad magician!'        
    st2 = 'Case #' + str(i+1) + ': ' + str(ans) + "\n"    
    f2.write(st2)

f2.close()
f1.close()      