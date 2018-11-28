#t = int(input())

#for i in range(0, t):
#    n.append(input())

with open('B-small-attempt0.in') as fil:
    n = fil.readlines()

#for i in range(0, len(n)):
#   n[i] = list(n[i])

for i in range(0, len(n)):
    j = int(n[i])
    while j > 0:
        j = str(j)
        if len(j) == 1:
            with open('B-small-attempt0.out', 'a') as res:
                res.write('Case #' + str(i + 1) + ': ' + str(j) + '\n')
            break
        else:
            for l in  range(0, len(j)-1):
                if 0 in list(j[l]) or j[l] > j[l+1]:
                    break
                elif l == len(j) - 2:
                    with open('B-small-attempt0.out', 'a') as res:
                        res.write('Case #' + str(i + 1) + ': ' + str(j) + '\n')
                    del j
                    j = 0
                    break
        j = int(j) - 1
