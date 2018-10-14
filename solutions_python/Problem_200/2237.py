T=  int(raw_input())
for t in xrange(T):
    num = map(int, list(raw_input()))
    output = []
    prev = 0 
    dec = False
    for v in num:
        if dec:
            output.append(9)
        else:
            if v < prev: 
                output[-1] -= 1
                dec = True
                nxt = output[-1]
                for r in xrange(len(output)-2, -1, -1):
                    if nxt < output[r]:
                        output[r+1] = 9
                        output[r] -= 1
                    nxt = output[r]
                output.append(9)

            else:
                output.append(v)
        prev = v
    print "Case #%d: %d" % (t+1, int("".join(map(str, output))))


