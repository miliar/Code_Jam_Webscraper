import io

def main(cas):
    data = raw_input().split()
    pa = pb = 1
    ta = tb = 0
    r = 0
    for i in range(int(data[0])):
        ii = i*2 + 1
        tget = int(data[ii+1])
        if data[ii].strip() == "O":
            tm = max(ta + abs(pa - tget), tb) + 1
            pa = tget
            ta = tm
            r = max(r, tm)
        else:
            tm = max(tb + abs(pb - tget), ta) + 1
            pb = tget
            tb = tm
            r = max(r, tm)
    print "Case #" + str(cas) + ": " + str(r)


if __name__=="__main__":
    cas = int(input())
    for i in range(cas):
        main(i+1)
