#!/usr/bin/python




if __name__ == "__main__":
    t = int(input())
    for test in range(t):
        d,n  = raw_input("").split(" ")
        d = int(d)
        n = int(n)
        k = []
        s = []
        for horse in range(n) :
            ki, si = raw_input("").split(" ")
            k.append(int(ki))
            s.append(int(si))

        # idx_min = s.index(min(s))
        # dist = d - k[idx_min]
        # time = float(dist)/float(min(s))
        # max_speed = float(d)/time


        speed = []
        for i in range(n):
            dist = d - k[i]
            time = float(dist)/float(s[i])
            speed.append(float(d)/time)
        print "Case #{}: {:.6f}".format(test+1, min(speed))