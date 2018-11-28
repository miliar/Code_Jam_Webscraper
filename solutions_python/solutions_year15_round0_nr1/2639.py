with open('A-large.in', 'r') as f,\
        open('A-large.out', 'a') as r:
    lineIndex = 0
    for line in f.readlines()[1:]:
        lineIndex += 1
        line = line.strip()
        s_max = line.split()[0]
        s = line.split()[1]

        standing = 0
        friends = 0
        for i in range(int(s_max) + 1):
            if i <= standing:
                standing += int(s[i])
            else:
                friends += i - standing
                standing = i + int(s[i])
        r.write("Case #%i: %i\n" % (lineIndex, friends))
