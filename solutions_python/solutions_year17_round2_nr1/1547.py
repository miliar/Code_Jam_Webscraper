cases = []


def meetingtime(a, b):
    ina, spa = a
    inb, spb = b
    if (spa - spb) == 0:
        return 999999999999999999999999999999999999999999
    return (inb - ina) / (spa - spb)


def meetingplace(a, b):
    ina, spa = a
    time = meetingtime(a, b)
    return ina + spa * time


with open("/Users/manuel/Desktop/test/codejam/1B/A/A-large.in", "r") as f:
    inp = f.read().split("\n")

    ncases = int(inp[0])
    findex = 1
    ccasenr = 1
    for casenr in range(ncases):
        case = []
        dest, horses = (int(x) for x in inp[findex].split(" "))
        findex += 1

        for row in range(horses):
            case.append(tuple(float(x) for x in inp[findex].split(" ")))
            findex += 1

        case = sorted(case, key=lambda t: (-t[0], -t[1]))

        slowest = (dest + 1.0, 1.0)
        for pos in range(len(case)):
            if meetingplace(slowest, case[pos]) > dest or meetingtime(slowest, case[pos]) < 0:
                slowest = case[pos]

        t = (dest - slowest[0]) / slowest[1]
        speed = dest / t

        print("Case #" + str(ccasenr) + ": " + str(speed))
        ccasenr += 1
