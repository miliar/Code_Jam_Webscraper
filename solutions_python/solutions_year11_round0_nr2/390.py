# Google Code Jam Qualification Round 2011
# Problem B. Magicka
# Varot Premtoon 7 May 2554

T = input()

for I in range(T):
    line = raw_input().split()
    c = int(line[0])
    if (c == 0):
        combines = []
    else:
        combines = line[1:c+1]
    d = int(line[c+1])
    if (d == 0):
        opposes = []
    else:
        opposes = line[c+2:c+2+d]
    #print(combines)
    #print(opposes)
    n = int(line[-2])
    invoke = line[-1]
    elist = []
    for ele in invoke:
        elist.append(ele)
        if (len(elist) == 1):
            continue
        for combine in combines:
            if ((elist[-1] == combine[0] and elist[-2] == combine[1]) or
                (elist[-1] == combine[1] and elist[-2] == combine[0])):
                elist[-2:] = combine[-1]
                break
        for oppose in opposes:
            if (oppose[0] in elist and oppose[1] in elist):
                elist = []
                break
        #print('after ' + ele + ' = ' + str(elist))
    output = 'Case #' + str(I+1) + ': ['
    if (len(elist) > 0):
        output += elist[0]
    for char in elist[1:]:
        output += ', ' + char
    output += ']'
    print(output)
        