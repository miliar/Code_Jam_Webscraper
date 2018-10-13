from sys import stdin

def main():
    cases = int(stdin.readline())
    for i in range(0, cases):
        total, added = 0, 0
        input_line = stdin.readline()
        tokens = input_line.split()
        smax = int(tokens[0])
        roll_call = []
        for x in range(0, smax + 1):
            roll_call.append(int(tokens[1][x]))

        for x in range(0, smax):
            total = total + roll_call[x]
            if roll_call[x+1] > 0:
                if total < x + 1:
                    diff = x + 1 - total
                    total = total + diff
                    added = added + diff

        print "Case #%s: %s" % ((i+1), added)

if __name__ == '__main__':
    main()
