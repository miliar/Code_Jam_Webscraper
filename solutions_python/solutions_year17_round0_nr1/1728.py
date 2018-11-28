t = int(raw_input().strip())


def flip_str(string):
    new_string = ''
    for char in string:
        if char == '+':
            new_string += '-'
        else:
            new_string += '+'
    return new_string

for i in range(t):
    pancake_string, k = raw_input().strip().split(' ')
    flips = 0
    for point in range(len(pancake_string) + 1 - int(k)):
        if pancake_string[point] == '+':
            continue
        else:
            flips += 1
            pancake_string = pancake_string[:point] + flip_str(pancake_string[point:point+int(k)]) + \
                             pancake_string[point+int(k):]

    if '-' in pancake_string:
        print "Case #{0}: IMPOSSIBLE".format(i+1)
    else:
        print "Case #{0}: {1}".format(i+1, flips)
