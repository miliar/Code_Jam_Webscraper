#!/usr/bin/python3

# Sounds like RLE-ing the strings might help?
# Should be the first check, re-encode the strings as (char, count)

def debug(*args, **kwargs):
    # print(*args, **kwargs)
    pass

cases = int(input())

def encode(str):
    char = str[0]
    ret = []
    count = 0
    for c in str:
        if char == c:
            count += 1
        else:
            ret.append((char, count))
            count = 1
            char = c
    ret.append((char, count))
    return ret

for case in range (1, cases + 1):
    scount = int(input())
    strings = []
    for s in range(scount):
        strings.append(input().strip())
    encoded = [encode(str) for str in strings]
    debug(encoded)

    # Two string only case!
    steps = 0
    impossible = False
    len0 = len(encoded[0])
    for str in encoded:
        if len(str) != len0:
            impossible = True
            break
    if impossible:
        debug("Length mismatch")
        print("Case #%s: %s" % (case, "Fegla Won"))
        continue

    for i in range(len(encoded[0])):
        lens = []
        for str in encoded:
            if str[i][0] != encoded[0][i][0]:
                impossible = True
                break
            lens.append(str[i][1])
        if impossible:
            break
        lens.sort()

        # Number of steps will be... median mean something something!
        # minimum distance to... uhh... 
        # Hrmmmm, add one char to all the shortest, subtract one from the
        # longest...
        # More like, do that for the _fewest_
        while True:
            bottom = 0
            for x in lens:
                if x == lens[0]:
                    bottom += 1
                else:
                    break
            if bottom == len(encoded):
                break
            top = 0
            lens.reverse()
            for x in lens:
                if x == lens[0]:
                    top += 1
                else:
                    break
            lens.reverse()
            if bottom > top:
                idx = len(lens) - 1
                for x in range(top):
                    steps += 1
                    lens[idx] -= 1
                    idx -= 1
            else:
                for x in range(bottom):
                    steps += 1
                    lens[x] += 1

        # steps += abs(encoded[0][i][1] - encoded[1][i][1])
    if impossible:
        steps = "Fegla Won"

    print("Case #%s: %s" % (case, steps))

