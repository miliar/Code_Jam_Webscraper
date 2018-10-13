

def findTidy(strTidy):
    resultV = True

    if strTidy.__len__() == 1:
        return resultV

    for idx in range(strTidy.__len__()-1):
        if int(strTidy[idx]) > int(strTidy[idx+1]):
            resultV = False
            break

    return resultV


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = raw_input()
        lNum = list(str(n))

        while True:
            for idx in range(lNum.__len__() - 1):
                if lNum[idx] > lNum[idx + 1]:
                    lNum[idx] = str(int(lNum[idx]) - 1)
                    for loop in range(idx + 1, lNum.__len__()):
                        lNum[loop] = "9"

            if findTidy("".join(lNum)):
                break

        print "Case #{}: {}".format(i, int("".join(lNum)))

main()