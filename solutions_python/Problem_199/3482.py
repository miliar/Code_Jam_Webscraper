import sys

flip_counter = 0

with open(sys.argv[1], 'r') as f:
    next(f)
    case = 0
    K = 0


    def flip(position, number, pancakes):
        global flip_counter
        flip_counter = flip_counter + 1
        to = number + position
        if position+number > len(pancakes):
            to = len(pancakes)-position-1

        for i in range(position, to):
            if pancakes[i] == '-':
                pancakes[i] = '+'
            else:
                pancakes[i] = '-'

    for line in f:
        flip_counter = 0
        case = case + 1

        splitted = line.split()
        pancakes = list(splitted[0])
        K = int(splitted[1])

        if not "-" in pancakes:
            print("Case #%d: 0" % (case,))
            continue

        i = 0
        for c in pancakes:
            if c=='-':
                flip(i,K,pancakes)
            i=i+1

        if "-" in pancakes:
            print ("Case #%d: IMPOSSIBLE" % (case,))
        else:
            print ("Case #%d: %d" % (case,flip_counter))