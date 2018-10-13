
def findMaxFilp(s,pancakes):
    idx = 0
    retV = 0
    temp = list(s)
    while True:
        if idx >= temp.__len__():
            break

        if temp[idx] == "-":
            if temp.__len__() - idx >= pancakes:
                retV += 1
                for loop in range(pancakes):
                    if temp[idx + loop] == "+":
                        temp[idx + loop] = "-"
                    else:
                        temp[idx + loop] = "+"
            else:
                retV = "Impossible"
                break

        idx += 1

    return retV


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, m = [str(s) for s in raw_input().split(" ")]
        temp = findMaxFilp(n,int(m))
        print "Case #{}: {}".format(i, temp)



main()