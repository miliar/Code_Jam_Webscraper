import sys

case = 0

with open(sys.argv[1]) as file:
    next(file)
    for line in file:
        case += 1
        N = int(line.split(" ")[0])
        K = int(line.split(" ")[1])
        stalls = list("1" + ("0" * N) + "1")

        if N == K:
            print "Case #" + str(case) + ": 0 0"
            continue

        for i in range(0, K):
            SLR = [-1, -1, -1]
            for s in range(1, N + 1):
                if (stalls[s] == "1"):
                    continue
                l = 0
                for j in range(s - 1, -1, -1):
                    if stalls[j] == "0":
                        l += 1
                    else:
                        break
                r = 0
                for j in range(s + 1, N + 2, 1):
                    if stalls[j] == "0":
                        r += 1
                    else:
                        break
                if SLR[0] == -1:
                    SLR[0] = s
                    SLR[1] = l
                    SLR[2] = r
                else:
                    if min([l, r]) > min([SLR[1], SLR[2]]):
                        SLR[0] = s
                        SLR[1] = l
                        SLR[2] = r
                    elif min([l, r]) == min([SLR[1], SLR[2]]):
                        if max([l, r]) > max([SLR[1], SLR[2]]):
                            SLR[0] = s
                            SLR[1] = l
                            SLR[2] = r
            L = max([SLR[1], SLR[2]])
            R = min([SLR[1], SLR[2]])
            stalls[SLR[0]] = "1"

            #print stalls
        #break

        print "Case #" + str(case) + ": " + str(L) + " " + str(R)
        #break
