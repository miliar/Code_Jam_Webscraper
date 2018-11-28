def rows_to_dict(f):
    row = int(f.readline())
    for i in range(4):
        stuff = f.readline()
        if i+1 == row:
            result = set([int(s) for s in stuff.split()])
    return result

f = open("a.test", "r")
num_tests = int(f.readline())
for i in range(num_tests):
    a = rows_to_dict(f)
    b = rows_to_dict(f)
    intersect = a & b
    s = "Case #" + str(i+1) + ": "
    if len(intersect) > 1:
        print s + "Bad magician!"
    elif len(intersect) == 0:
        print s + "Volunteer cheated!"
    else:
        print s + str(intersect.pop())
