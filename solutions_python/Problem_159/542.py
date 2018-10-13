# Google Code Jam 2015

def sum_dips(ls):
    mintot = 0
    for i in range(len(ls) - 1):
        curr = ls[i]
        nxt = ls[i + 1]
        if nxt < curr:
            mintot += curr - nxt
    return mintot

def get_min_eat_rate(ls):
    max_rate = 0
    for i in range(len(ls) - 1):
        curr = ls[i]
        nxt = ls[i + 1]
        if curr - nxt > max_rate:
            max_rate = curr - nxt
    return max_rate / 10.0

def sum_second_method(ls):
    r = get_min_eat_rate(ls)
    fats = 0

    eaten_per_batch = r * 10
    for i in range(len(ls) - 1):
        curr = ls[i]
        if 10 * r > curr:
            fats += curr
        else:
            fats += 10 * r
    return fats

def unit_tests():
    assert sum_dips([10, 5, 15, 5]) == 15
    assert sum_dips([10, 10]) == 0
    assert sum_dips([10]) == 0
    assert sum_dips([10, 15]) == 0

    assert get_min_eat_rate([10, 5, 15, 5]) == 1
    assert get_min_eat_rate([10, 10]) == 0
    assert get_min_eat_rate([10, 5, 30, 5]) == 2.5

    assert sum_second_method([10, 5, 15, 5]) == 25


def generate_result(fname):
    assert type(fname) == str
    s = ""
    lines = open(fname).readlines()[1:]
    assert len(lines) > 1 and "Need to set up input file and gold file"
    casenum = 1
    for i, l in enumerate(lines):
        if i % 2 == 0:
            continue
        l = l.strip()
        vals = [int(i) for i in l.split()]
        s += "Case #{}: {} {}\n".format(casenum, sum_dips(vals), int(sum_second_method(vals)))
        casenum += 1
    print s
    return s

def test_e2e(input_fname, correctfname):
    f = open(correctfname)
    myans = generate_result(input_fname)
    key = "".join(f.readlines())
    print key
    assert myans == key

def run_tests():
    test_e2e("testin.txt", "testout.txt.gold")
    unit_tests()
    print "Tests passed."

def gen_output(infilename):
    downloadsdirectory = "/Users/robertkarl/Downloads/"
    answer = generate_result(downloadsdirectory + infilename)
    outfile = open(downloadsdirectory + "ans.txt", 'w')
    outfile.write(answer)
    outfile.close()



if __name__ == "__main__":
    run_tests()
    infilename = "A-large.in"
    gen_output(infilename)

