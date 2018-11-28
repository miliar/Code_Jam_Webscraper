def b(C,F,X,R=2.0):
    def buy(target):
        t , p= 0, 0
        p = C / R
        t += p
        t += target / (R + F)
        return t, p

    def wait(target):
        return (target - totalCookies) / R

    target = X
    totalCookies = 0
    t = 0
    while totalCookies != X:
        buyTime, buyCost = buy(target)
        wTime = wait(target)
        if buyTime < wTime:
            t += buyCost
            R += F
        else:
            t += wTime
            totalCookies += target - totalCookies
            return "{:.7f}".format(t)
        


FILENAME = "B-large"
f = open(FILENAME + '.in', 'r')
T = int(f.readline())
output = []

for i in range(T):
    temp = map(float,f.readline().split(' '))
    C = temp[0]
    F = temp[1]
    X = temp[2]

    output.append("Case #"+str(i+1)+": " + str(b(C,F,X)))
    print output[i]


f.close()
output = '\n'.join(e for e in output)
f = open(FILENAME + '.out', 'w')
f.write(output)
f.close()

