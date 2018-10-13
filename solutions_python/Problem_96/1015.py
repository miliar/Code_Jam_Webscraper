def main():
    cases = int(raw_input())
    for i in range(cases):
        line = raw_input()
        splits = line.split()
        dancers = int(splits[0])
        surprises = int(splits[1])
        point = int(splits[2])
        scores = map(int, splits[3:])
        sure = 0
        maybe = 0
        for s in scores:
            lowpoint1 = point-1
            lowpoint2 = point-2
            if lowpoint1 < 0:
                lowpoint1 = 0
            if lowpoint2 < 0:
                lowpoint2 = 0
            if s >= point + lowpoint1 * 2:
                sure += 1
            elif s >= point + lowpoint2 * 2:
                maybe += 1
        #print sure, maybe, surprises
        if maybe > surprises:
            maybe = surprises
        output = str(sure + maybe)
        print "Case #%d: %s" % (i+1, output)

if __name__ == "__main__":
    main()
