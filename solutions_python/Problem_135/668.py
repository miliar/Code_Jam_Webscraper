import fileinput

def read_line(it):
    target_line = int(it.next())
    for i in range(target_line-1):
        it.next()
    line_set = set([int(x) for x in it.next().split()])
    for i in range(4-target_line):
        it.next()
    return line_set

def solve_case(it):
    first_set = read_line(it)
    second_set = read_line(it)
    intersect = list(first_set & second_set)
    if len(intersect) == 1:
        return str(intersect[0])
    elif len(intersect) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

def main():
    it = fileinput.input()
    num_cases = int(it.next())
    for i in range(num_cases):
        print "Case #%d: %s" % (i+1,solve_case(it))

if __name__ == "__main__":
    main()
