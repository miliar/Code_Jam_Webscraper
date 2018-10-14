import sys

def main():
    lines = sys.stdin.read().split("\n")

    for casenum, line in enumerate(lines[1:]):

        y = line.split(" ")
        if(len(y)<2):
            continue
        test, snum = y
        num = int(snum)

        test = [t == "+" for t in test]

        count = 0
        for it in range(len(test) - num + 1):
            if not test[it]:
                for iit in range(num):
                    test[iit + it] = not test[iit + it]
                count += 1



        if all(test[-num:]):
            print "Case  #{}: {}".format(casenum + 1, count)
        else:
            print "Case  #{}: IMPOSSIBLE".format(casenum + 1)




if __name__ == "__main__":
    main()
