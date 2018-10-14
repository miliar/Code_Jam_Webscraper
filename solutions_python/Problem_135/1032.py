T = int(raw_input())
def read_nums():
    line_no = int(raw_input())
    lines = [map(int,raw_input().split()) for _ in "A"*4]
    return set(lines[line_no-1])
for i in xrange(T):
    s = read_nums() & read_nums()
    if len(s) == 1:
        res = str(list(s)[0])
    elif not s:
        res = "Volunteer cheated!"
    else:
        res = "Bad magician!"
    print "Case #%d: %s" % (i+1, res)
