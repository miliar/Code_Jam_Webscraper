import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    f = open("b.out", 'w')

    for i in range(1, T+1):
        line = sys.stdin.readline().split()
        C = float(line[0])
        F = float(line[1])
        X = float(line[2])
        t = 0
        cookie_speed = 2

        if C >= X:
            f.write("Case #%d: %f\n" %(i, X/2))
        else:
            while 1:
                t_farm = C / cookie_speed
                t += t_farm
                t_complete = (X - C) / cookie_speed
                if t_complete <= X / (cookie_speed + F):
                    t += t_complete
                    f.write("Case #%d: %f\n" %(i, t))
                    break
                else:
                    cookie_speed += F

    f.close()

