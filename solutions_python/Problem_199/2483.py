x = int(input())
for i in range(x):
    q = input()
    init = "Case #" + str(i+1) + ": "
    pani = ""
    done = False
    k = 0
    for j in range(len(q)):
        if not done and q[j] != " ":
            pani += q[j]
        elif not done:
            done = True
            k = int(q[j+1:])
            break
    pan = []
    for j in range(len(pani)):
        if pani[j] == '+':
            pan.append(1)
        else:
            pan.append(0)
    count = 0
    z = 0
    while True:
        try:
            z = pan.index(0)
        except:
             print(init + str(count))
             break
        if z + k > len(pan):
            print(init + "IMPOSSIBLE")
            break
        else:
            for p in range(z, z+k):
                pan[p] = 1 - pan[p]
            count += 1




            
