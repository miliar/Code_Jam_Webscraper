
def count_recycles(x, min, max):
    total = 0
    thing_to_put_in_front = ""
    for c in x[::-1]:
        thing_to_put_in_front = c + thing_to_put_in_front
        new = thing_to_put_in_front + x[:-len(thing_to_put_in_front)]
        if (new != x and (len(str(int(new))) == len(str(int(x))))):
            if (int(new) >= min and int(new) <= max and int(x) < int(new)):
                total += 1
    return total


def count_recycles_between(min, max):
    total = 0
    for x in range(min, max+1):
        total += count_recycles(str(x), min, max)
    return total


in_file = open("qualC.small.in")

in_file.readline()

ind = 1
for line in in_file:
    if (line[-1] == "\n"):
        line = line[:-1]
    print "Case #%d: %s" % (ind, count_recycles_between(int(line.split(" ")[0]), int(line.split(" ")[1])))
    ind += 1




        
