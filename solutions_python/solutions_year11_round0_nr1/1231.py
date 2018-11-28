
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
n = int(fin.readline())
for i in range(n):
    st = fin.readline()
    t = st.split()
    t_t = 0
    robots = {'O':[1,0,0], 'B':[1,0,0]}
    prev = t[1]
    for j in range(int(t[0])): 
        robot = t[2*j+1]
        loc = int(t[2*j+2])
        robots[robot][1] = 0
        if robot != prev: robots[robot][2]=0
        temp_t = abs(loc - robots[robot][0])
        if (robot != prev):
            if ((temp_t - robots[prev][2])>0):
                temp_t -= robots[prev][2]
            else:
                temp_t = 0
        temp_t += 1
        t_t += temp_t
        robots[robot][0] = loc
        robots[robot][1] = temp_t
        robots[robot][2] += temp_t
        prev = robot
    fout.write('Case #'+str(i+1)+': '+str(t_t)+'\n')

fin.close()
fout.close()


