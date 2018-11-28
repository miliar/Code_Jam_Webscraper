f1 = open('ovation.in')
f2 = open('ovation.out', mode = "w")
i = 0
for line in f1 :
    i += 1
    line = line[:-1]
    if i == 1 :
        T = int(line)
        S = []
    else:
        l = line.split()
        S.append([int(x) for x in l[1]])

res = []
for i in S :
    friends = 0
    stand_up = 0
    for idx,j in enumerate(i) :
        if j > 0 :
            if stand_up < idx :
                friends += idx - stand_up
                stand_up = idx
            stand_up += j
    res.append(friends)

for i in range(T):
    st = 'Case #' + str(i+1) + ': ' + str(res[i]) + "\n"    
    f2.write(st)

f2.close()
f1.close()