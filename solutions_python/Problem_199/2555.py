file = open("/mnt/c/Users/Samantha Chhoeu/Desktop/2017_Code_Jam/QualificationRound/input.txt")
t =0
# convert string to list
def convert(S):
    list = []
    for char in S:
        if char is "+":
            # 1
            list.append(1)
        elif char is "-":
            # 0
            list.append(0)
    return list

def flip(pancakes, k):
    i = 0
    flips = 0
    while i < len(pancakes):
        pancake = pancakes[i]
        if pancake == 1:
            i += 1
            continue
        # impossible
        if len(pancakes) < i + k:
            return -1
        # flip from i and k pancakes in front
        for j in range(k):
            pancakes[i + j] = (pancakes[i + j] + 1) % 2

        # next pancake
        flips += 1
        i += 1
    return flips
i = 0
for line in file:
    this_count = 0
    if t == 0:
        t = line
    else:
        line = line.split()
        s = line[0] # string
        k = int(line[1]) # integer

        pancakes = [] # pancake list
        pancakes = convert(s)

        # flip
        flips = flip(pancakes, k)

        answer = flips
        if answer == -1:
            answer = 'IMPOSSIBLE'

        print "case #"+str(i)+":",answer
    i+=1
