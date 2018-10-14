from collections import deque
import sys

if __name__ == '__main__':
    f = open(sys.argv[1])
    t = int(f.readline())

    for i in range(t):
        n = int(f.readline())
        schedules = deque()
        for j in range(n):
            schedules.append(f.readline())
        wp = deque()
        for s in schedules:
            count = 0
            num = 0
            for c in s:
                if c == '1':
                    count = count + 1
                    num = num+1
                elif c == '0':
                    num = num+1
            wp.append(float(count)/float(num))

        owp = []
        for j,s in enumerate(schedules):
            t_count = 0
            total = 0.0
            for k,item in enumerate(s):
                if item == '0' or item == '1':
                    os = schedules[k]
                    count = 0;
                    num = 0;
                    for l in range(len(os)):
                        if l == j:
                            continue
                        if os[l] == '1':
                            count = count+1
                            num = num+1
                        elif os[l] == '0':
                            num = num + 1
                    total = (float(count)/float(num)) + total
                    t_count = t_count+1
            owp.append(float(total)/float(t_count))
        oowp = []
        for s in schedules:
            t_count = 0
            total = 0.0
            for j,item in enumerate(s):
                if item == '0' or item == '1':
                    t_count = t_count + 1
                    total = total + owp[j]
            oowp.append(float(total) / float(t_count))
        total = []
        for j in range(n):
            total.append(0.25*wp[j]+0.5*owp[j]+0.25*oowp[j])
        print 'Case #%d:'%(i+1)
        for val in total:
            print val

            
        
