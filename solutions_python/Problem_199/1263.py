with open("oversized_pancake_flipper.large", 'r') as f:
    lines = f.read().strip().split('\n')
    testcases = int(lines[0])
    for case in xrange(1, testcases + 1):
        tokens = lines[case].split(' ')
        pancakes = list(tokens[0])
        k = int(tokens[1])
        possible = True
        flips = 0
        for i in xrange(len(pancakes) - k + 1):
            if pancakes[i] == '-':
                for j in xrange(k):
                    pancakes[i+j] = '+' if pancakes[i+j] == '-' else '-'
                flips += 1
                #print pancakes
        for i in xrange(len(pancakes) - k, len(pancakes)):
            if pancakes[i] == '-':
                possible = False
                break
        print("Case #%s: %s" % (str(case), str(flips) if possible else 'IMPOSSIBLE'))
