


def generate(start):
    n = list(start)

    num = []
    if len(n) == 1:
        return start
    else :

        for i in xrange(len(n)):

            for j in xrange(int(n[i]),0,-1):
                if i > 0:
                    if int(n[i]) >= j and int(n[i-1]) <= int(n[i]):
                        num.append(str(j))
                        break
                else :
                    if int(n[i]) >= j:
                        num.append(str(j))
                        break

    return ("".join(num) if len(num) == len(n) else generate(s(start)))
def s(start):
    x = list(start)
    for i in xrange(len(x)-1):
        if int(x[i]) > int(x[i+1]):
            x[i + 1] = str(9)
            if int("".join(x)) > int(start):
                x[i] = str(int(x[i]) - 1)










    if int(x[0]) == 0:
        x.pop(0)

    return "".join(x)
with open("/home/gifty/PycharmProjects/GKJ/B-large.txt") as f:
    n = int(f.readline())
    lines = f.readlines()
    i = 1
    for line in lines:

        x = generate(str(line.strip()))
        print "Case  #%s:"%(i),x
        i += 1






