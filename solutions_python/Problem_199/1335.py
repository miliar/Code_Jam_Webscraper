def flip(start, length, arr):
    for i in range (length):
        current = i + start
        if arr[current] == '+':
            arr[current] = '-'
        else:
            arr[current] = '+'
    return(arr)

def all_flipped(arr):
    is_flipped = True
    i = 0
    while(is_flipped and i < len(arr)):
        is_flipped = arr[i] == '+'
        i += 1
    return(is_flipped)

infile = open("A-large.in", 'r')
out = open("outuput.txt", 'w')
num_prob = int(infile.readline())
i = 0
for line in infile:
    i += 1
    pan, width = [str(s) for s in line.split(" ")]
    pan = list(pan)
    width = int(width)
    current = 0
    count = 0
    while (current <= len(pan) - (width)):
        #print(pan[current], current)
        if (pan[current] == '-'):
            count += 1
            pan = flip(current, width, pan)
        current += 1
    over = all_flipped(pan)
    if (over):
        val = "Case #{}: {}\n".format(i, count)
    else:
        val = "Case #{}: IMPOSSIBLE\n".format(i)
    out.write(val)
infile.close()
out.close()