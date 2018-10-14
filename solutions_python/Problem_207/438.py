def output(t, res):
    casestr = "Case #" + str(t+1) +": "
    status = str(res) if res != None else "IMPOSSIBLE"
    outputLine = casestr+status
    print outputLine


def max_combo(R, Y, B):
    m = min(R, Y, B)
    if m == B:
        return "R", "Y"
    elif m == Y:
        return "R", "B"
    else:
        return "Y", "B"


def max_one(R, Y, B):
    m = max(R, Y, B)
    if m == B:
        return "B"
    elif m == Y:
        return "Y"
    else:
        return "R"


def go_more(R, Y, B):
    m = filter(lambda x: x > 0,  [R, Y, B])
    return len(m) > 1


def main():
    T = int( raw_input() )

    for t in xrange(T):
        N,R,O,Y,G,B,V = map(int, raw_input().split(' '))
        stalls = []
        last = "?"
        while go_more(R, Y, B):
            combo = max_combo(R, Y, B)
            if last != combo[0]:
                stalls.append(combo[0])
                stalls.append(combo[1])
                last = combo[1]
            else:
                stalls.append(combo[1])
                stalls.append(combo[0])
                last = combo[0]

            if "R" in combo:
                R -= 1
            if "Y" in combo:
                Y -= 1
            if "B" in combo:
                B -= 1

        if R + Y + B >= 2:
            output(t, None)
        elif R + Y + B == 0:
            if last == stalls[0]:
                output(t, None)
            else:
                output(t, "".join(stalls))
        else: # 1
            one = max_one(R, Y, B)
            if one == stalls[0]:
                output(t, None)
            elif one == last:
                output(t, None)
            else:
                stalls.append(one)
                output(t, "".join(stalls))


if __name__ == "__main__":
    main()