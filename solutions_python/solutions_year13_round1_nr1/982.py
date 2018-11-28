def findNumber(r, t):
    count = 0
    p = 0
    done = False
    while not done:
        y = (2*r) + (2*p) + 1
        if t >= y:
            t -= y
            count += 1
        else:
            done = True
        p += 2
    return count



FILENAME = "A-small-attempt0"
f = open(FILENAME + '.in', 'r')
T = int(f.readline())
output = []
for i in range(T):
    temp = f.readline().split(' ')
    r = int(temp[0])
    t = int(temp[1])

    
    output.append("Case #"+str(i+1)+": " + str(findNumber(r,t)))
    print output[i]
    


f.close()
output = '\n'.join(e for e in output)
f = open(FILENAME + '.out', 'w')
f.write(output)
f.close()
