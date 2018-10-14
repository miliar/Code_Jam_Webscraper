def main():
    with open('test.in','r') as f:
        line, outputs = f.readline(), []
        for x, line in enumerate(f):
            x += 1
            l = line.split()
            n, k = int(l[0]), int(l[1])
            light, power, on, off = "OFF", set([1]), set(), set(range(1,n+2))
            for i in xrange(k):
                off, on = power^off, power^on
                try:
                    power = set(range(1,1+(min(off))))
                except:
                    power = set(range(1,1+(len(on))))
            if n in on.intersection(power):
                light = "ON"
            s = "Case #{0}: {1}".format(x, light)
            print s
            outputs.append(s)
    with open('test.out','w') as g:
        g.write('\n'.join(outputs))

if __name__ =='__main__':
    main()
