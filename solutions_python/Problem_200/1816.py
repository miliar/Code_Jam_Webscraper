if __name__ == "__main__":
    n = int(raw_input())
    for i in range(n):
        x = int(raw_input())
        if x % 10 == 0:
            x -= 1
        x = str(x)

        l = []

        for j in x:
            l.append(int(j))
        dirty = True
        while dirty:
            dirty = False
            for k in range(len(l) - 1):
                if l[k] > l[k+1]:
                    l[k] -= 1
                    dirty = True
                    for m in range(k+1, len(l)):
                        l[m] = 9

        if l[0] == 0:
            del l[0]
        l = [ str(p) for p in l ]
        print "Case #" + str(i+1) + ": " + "".join(l)
                
