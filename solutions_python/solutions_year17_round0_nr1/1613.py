# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def rev(cakes,pan):
    for i in range(1,pan+1):
        if cakes[-i]=='+':
            cakes[-i]='-'
        else:
            cakes[-i]='+'
    return cakes

T = int(raw_input())  # read a line with a single integer

for i in xrange(1, T + 1):
#    line = raw_input().split()
#    flip_str = line[0]
#    pan = line[1]

    all_str = raw_input().split()
    flip_str = all_str[0]
    flip_len = len(flip_str)
    pan = int(all_str[1])

    if '-' not in flip_str:
        print "Case #"+str(i)+": 0"
        continue

    cakes = list(flip_str)

    count = 0
    while len(cakes) > pan:
        if cakes[-1] == '+':
            cakes.pop()
        else:
            cakes = rev(cakes,pan)
            count += 1

    if not '-' in cakes:
        print "Case #"+str(i)+": "+str(count)
    elif not '+' in cakes:
        print "Case #"+str(i)+": "+str(count+1)
    else:
        print "Case #"+str(i)+": IMPOSSIBLE"
