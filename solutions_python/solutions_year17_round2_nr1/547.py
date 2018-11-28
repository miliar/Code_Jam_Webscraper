def cruise(test):
    D = int(test[0])
    N = int(test[1])
    horses = test[2]
    #print D, N, horses
    for i in range(N):
        print horses[i]
    max_speed = 1.0*10**19
    for i in range(N-1,-1,-1):
        #treat horses in back order
        speed = 1.0*D/ ((1.0*D-int(horses[i][0]))/int(horses[i][1]))
        if speed<max_speed:
            max_speed=speed
    return '{:7f}'.format(max_speed)
f = open('input.in', 'r')
T = int(f.readline())
tcs = []

for i in range(T):
    D, N = f.readline().split(' ')
    horses = []
    for i in range(int(N)):
        horses.append(f.readline().split(' '))

    tcs.append([D, N, horses])

f.close()
f = open('output.txt', 'w')
for i in range(T):
    f.write("Case #%s: %s\n" % (i+1, cruise(tcs[i])))
f.close()

