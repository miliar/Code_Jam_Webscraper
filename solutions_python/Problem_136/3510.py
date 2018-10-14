__author__ = 'gena'


def solver(filename):
    with open(filename) as f:
        T = int(f.readline())
        with open("solution", "w") as sol:
            for i in range(T):
                params = [float(p) for p in f.readline().split(" ")]
                C = params[0]
                F = params[1]
                X = params[2]
                perCookie = 2
                T = round(X / perCookie, 1)
                t = 0
                currentCookie = 0
                while True:
                    if C >= X:
                        t = round(X / 2, 7)
                        sol.write("Case #{0}: {1}\n".format(i + 1, t))
                        break
                    else:
                        t1 = round(C / perCookie, 7)
                        if round(X / (perCookie + F), 7) < round((X - C)/perCookie, 7):
                            t += t1
                            perCookie += F
                        else:
                            t += round((X - currentCookie) / perCookie, 7)
                            sol.write("Case #{0}: {1}\n".format(i + 1, round(t, 7)))
                            break



solver("small")