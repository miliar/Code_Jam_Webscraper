import sys

f = open(sys.path[0] + "//A-large.in")
all = f.readlines()
N = int(all.pop(0))
for i, line in enumerate(all):
    line = line.strip().split(" ")
    push=line[0]
    j = 1
    posO = 1
    posB = 1
    steps = 0
    while j < len(line):
        if line[j] == "O":
            # delam dokler ne pridem do prave stevilke
            # sproti premikam tudi B
            w = int(line[j+1])
            moves = abs(posO - w) + 1 # pritisnemo gumb
            posO = w
            steps += moves
            l = j+2
            while l < len(line) and line[l] != "B":
                l+=2
            if l < len(line):
                x = int(line[l+1]) # nova pozicija
                if x > posB:
                    if x - posB > moves:
                        posB += moves
                    else:
                        posB = x
                elif x < posB:
                    if posB - x > moves:
                        posB -= moves
                    else:
                        posB = x

        else:
            w = int(line[j+1])
            moves = abs(posB - w) + 1 # pritisnemo gumb
            posB = w
            steps += moves
            l = j+2
            while l < len(line) and line[l] != "O":
                l+=2
            if l < len(line):
                x = int(line[l+1]) # nova pozicija
                if x > posO:
                    if x - posO > moves:
                        posO += moves
                    else:
                        posO = x
                elif x < posO:
                    if posO - x > moves:
                        posO -= moves
                    else:
                        posO = x
        j+=2
    print "Case #" + str(i+1) + ":", steps
    
    