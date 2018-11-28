


def pancakes(line, flipSize):
    count = 0
    flipped = False
    flipCounter = 0
    i = 0
    output = list(line)
    canFlip = True
    while (i < len(line)):
        if len(line)-i == flipSize:
            if output[i] == '-':
                flip(i, flipSize, output)
                count += 1
        elif len(line) - i < flipSize:
            if output[i] == '-':
                return -1
        else:
            if output[i] == '-':
                flip(i, flipSize, output)
                count += 1
        i += 1
    return count

def flip(index, flipSize, output):
    while flipSize != 0:
        if output[index] == '-':
            output[index] = '+'
        else:
            output[index] = '-'
        index +=1
        flipSize-=1



t = int(raw_input())
for i in range(1 , t+1):
    line, size = raw_input().split(" ")
    size = int(size)
    output = pancakes(line, size)
    if output == -1:
        output = "IMPOSSIBLE"
        print("Case #{}: {}".format(i, output))
    else:
        print("Case #{}: {}".format(i, str(output)))
