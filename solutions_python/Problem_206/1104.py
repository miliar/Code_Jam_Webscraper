#!/usr/bin/python

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(0,t):
        s = raw_input()
        D = int(s.split()[0])
        N = int(s.split()[1])
        horses = []
        for j in range(0, N):
            s = raw_input()
            Ki = int(s.split()[0])
            Si = int(s.split()[1])
            time = float(D-Ki) / float(Si)
            horses.append(time)
        time = max(horses)
        speed = float(D) / time
        print "Case #" + str(i + 1) + ":", speed
        
