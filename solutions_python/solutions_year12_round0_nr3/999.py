def recycled(i, upper):
    num = i
    li = list(str(i))
    leng = len(li)
    li = li[:] + li[:-1]
    n = 0
    s = set()
    for j in range(leng):
        sub = li[j:leng+j]
        if sub[0] == '0':
            continue
        test = int(''.join(sub))
        if num < test <= upper:
            if test not in s:
                n += 1
                s.add(test)
            #print '(%d,%d)' % (num, test)
    return n

def main():
    cases = int(raw_input())
    for i in range(cases):
        line = raw_input()
        splits = line.split();
        lower = int(splits[0])
        higher = int(splits[1])
        n = 0
        for j in range(lower, higher):
            n += recycled(j, higher)
        output = str(n)
        print "Case #%d: %s" % (i+1, output)

if __name__ == "__main__":
    main()
