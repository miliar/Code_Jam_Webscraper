

def flip(strinput, index, sizeflipper):
    strinput = list(str(strinput)) # duplicate!
    for i in range(index,index+sizeflipper):
        if strinput[i] == "-":
            strinput[i] = '+'
        else:
            strinput[i] = '-'
    return ''.join(strinput)

def timesToFlip(pancake,sizeflipper):
    countFlipped = 0
    while len(pancake) > 0:
        if pancake[0] == '-':
            try:
                pancake = flip(pancake,0,sizeflipper)
                countFlipped += 1
            except:
                return "IMPOSSIBLE"
        pancake = pancake[1:]
    return str(countFlipped)

if __name__ == "__main__":
    with open('A-large.in') as file:
        for casenum,line in enumerate(file):
            if casenum == 0:
                continue
            pancake, sizeflipper = line.split()
            sizeflipper = int(sizeflipper)
            print("Case #%d: %s" % (casenum,timesToFlip(pancake,sizeflipper)))
