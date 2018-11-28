

def num_flips(pancakes, flipper):
    if '-' not in pancakes:
        return "0"
    elif flipper > len(pancakes):
        return "IMPOSSIBLE"
    else:
        flips = 0
        for i in range(len(pancakes) - flipper + 1):
            if pancakes[i] == '-':
                for j in range(i, i+flipper):
                    pancakes[j] = '+' if pancakes[j] == '-' else '-'
                flips += 1
        if '-' not in pancakes[-flipper:]:
            return str(flips)
        return "IMPOSSIBLE"

if __name__ == '__main__':
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, m = raw_input().split(" ") # read a list of integers, 2 in this case
        print "Case #{}: {}".format(i, num_flips(list(n), int(m)))
