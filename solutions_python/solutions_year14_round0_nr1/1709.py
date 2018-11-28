

def get_line(fp):
    answer = int(fp.readline())
    lines = []
    for line_no in range(1, 5):
        r = fp.readline()
        if line_no == answer:
            line = set(map(int, r.split(' ')))
    return answer, line

with open('in.txt') as fp:
    T = int(fp.readline())
    for t in range(1, T + 1):
        answer_a, line_a = get_line(fp)
        # print("line %d:" % (answer_a, ), line_a)
        answer_b, line_b = get_line(fp)
        # print("line %d:" % (answer_b, ), line_b)
        # print("-:", line_a & line_b)
        result = line_a & line_b
        if len(result) < 1:
            out = "Volunteer cheated!"
        elif len(result) == 1:
            out = "%d" % (result.pop(),)
        else:
            out = "Bad magician!"


        print("Case #%d: %s" % (t, out, ))
