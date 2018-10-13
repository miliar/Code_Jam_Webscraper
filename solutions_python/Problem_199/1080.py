with open('/Users/shawn/Documents/python_proj/codejam/A-large.in', 'r') as f:
    cases = int(f.readline())
    lines = f.readlines()

for case in range(cases):
    string, size = lines[case].strip().split(" ")

    k = int(size)
    i = 0
    count = 0
    possible = True
    pattern = []
    for s in string:
        pattern += [1] if s == "+" else [0]
    pattern_len = len(pattern)

    while i < (pattern_len - k + 1):
        if pattern[i] == 0:
            for j in range(k):
                pattern[i + j] ^= 1
            count += 1
        i += 1

    while i < len(pattern):
        if pattern[i] == 0:
            possible = False
            break
        i += 1

    if possible:
        print "Case #" + str(case+1) + ": " + str(count)
    else:
        print "Case #" + str(case+1) + ": "+"IMPOSSIBLE"