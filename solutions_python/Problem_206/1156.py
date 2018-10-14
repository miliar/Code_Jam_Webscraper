t = int(raw_input(''))
for test in range(t):
    s = raw_input('')
    s = s.split(' ')
    s[0] = int(s[0])
    s[1] = int(s[1])
    dist = s[0]
    horses = []
    for i in range(s[1]):
        s1 = raw_input('')
        s1 = s1.split(' ')
        s1[0] = int(s1[0])
        s1[1] = int(s1[1])
        horses.append(s1)
    time = []
    max_time = 0
    for i in range(s[1]):
        time_t = float(dist - horses[i][0])/horses[i][1]
        if time_t > max_time:
            max_time = time_t
    speed = s[0]/max_time
    print "Case #" + str(test+1) + ": " + str(speed)
        
        