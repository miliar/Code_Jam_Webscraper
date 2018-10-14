import os

h = open('sample.txt', 'r')
out = open('output.txt', 'w')

cases = int(h.readline())

for case in range(cases):
    n = int(h.readline().strip())
    scores = []
    wp = []
    owp = []
    oowp = []
    ans = []
    for i in range(n):
        temp = h.readline().strip()
        scores.append(list(temp))
        (w,t) = (0,0)
        for j in range(n):
            if(scores[i][j] == '1'):
                w = w + 1
                t = t + 1
            elif(scores[i][j] == '0'):    
                t = t + 1
        wp.append(1.0 * w/t)

    for i in range(n):
        owp.insert(i,0)
        temp = []
        no = 0
        for j in range(n):
            (w,t) = (0,0)
            temp.insert(j,0)
            if(scores[i][j] == '.'):
                continue
            for k in range(n):
                if(scores[j][k] != '.' and i != k):
                    if(scores[j][k] == '1'):
                        w = w + 1
                    t = t + 1
            if(t > 0):
                temp[j] = 1.0 * w/t
                no = no + 1
        if(no > 0):       
            owp[i] = 1.0 * sum(temp)/no

    for i in range(n):
        (temp,t) = (0,0)
        for j in range(n):
            if(scores[i][j] != '.'):
                temp = temp + owp[j]
                t = t + 1
        if(t > 0):
            oowp.insert(i, 1.0 * temp/t)
        else:
            oowp.insert(i, 0)
    
    for i in range(n):
        ans.insert(i, 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i])
    
    
    out.write('Case #' + str(case+1) + ':\n')
    for i in range(n):
        out.write(str(ans[i]) + '\n')

h.close()
out.close()


