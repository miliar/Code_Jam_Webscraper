def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n = str(raw_input())
        x = []
        for ch in n:
            x.append(int(ch))
        decode(x, i)
        
def decode(n, i):
    last_num = 0
    for dig in range(len(n)):
        if last_num <= n[dig]:
            last_num = n[dig]
            continue
        n[dig - 1] -= 1
        index = dig
        for back in range(dig - 1, 0, -1): # -2?
            if n[back - 1] <= n[back]:
                break
            index -= 1
            n[back - 1] -= 1
        for x in range(index, len(n)):
            n[x] = 9
        last_num = n[dig]
    s = 0
    for x in n:
        s *= 10
        s += x
    print "Case #%s: %s" % (i, s)

main()
