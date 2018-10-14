def boolify(s):
    return True if s == "+" else False

def strify(b):
    return "+" if b == True else "-"

def griddle_str(griddle):
    return "".join([strify(b) for b in griddle])

def flip(griddle, flipper):
    # solve from left to right
    if False in griddle:
        i = griddle.index(False)
        if i + flipper > len(griddle):
            i = len(griddle) - flipper
        for j in range(i, i+flipper):
            griddle[j] = not griddle[j]
    return griddle

def count_flips(griddle, flipper, flips=0, previous=[]):
    if all(griddle):
        return flips
    else:
        #previous.append(griddle)
        new_griddle = flip(griddle, flipper)
        flips+=1
        # print "This is old", griddle
        # print "This is new", new_griddle
        # print "all of old", previous
        # print flips, griddle_str(new_griddle)
        # if new_griddle in previous:
        #     return "IMPOSSIBLE"
        # else:
        return count_flips(new_griddle, flipper, flips=flips, previous=previous)

def main():
    # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        griddle, flipper = raw_input().split()
        # print griddle, "will use flipper of", flipper
        griddle_bool = [boolify(elem) for elem in griddle]
        try:
            flips = count_flips(griddle_bool, int(flipper))
        except:
            flips = "IMPOSSIBLE"
        print "Case #{}: {}".format(i, flips)

if __name__ == '__main__':
    main()
