import sys


def process_input(fin, fout):
    T = int(fin.readline().strip())
    print "T =", T

    for i in range(T):
        print "Case:", i
        process_case(fin, fout, i)
        fin.readline()


def process_case(fin, fout, case):
    diag1 = ''
    diag2 = ''
    c0 = ''
    c1 = ''
    c2 = ''
    c3 = ''
    empties = False
    result = ''
    for i in range(4):
        line = fin.readline().strip()
        result = result or process_line(line)
        diag1 += line[i]
        diag2 += line[3-i]
        c0 += line[0]
        c1 += line[1]
        c2 += line[2]
        c3 += line[3]
        if '.' in line:
            empties = True

    result = result or process_line(c0) or process_line(c1)
    result = result or process_line(c2) or process_line(c3)
    result = result or process_line(diag1) or process_line(diag2)
    if result:
        fout.write("Case #%d: " % (case + 1) + result + "\n")
        return

    if empties:
        fout.write("Case #%d: " % (case + 1) + "Game has not completed" + "\n")
    else:
        fout.write("Case #%d: " % (case + 1) + "Draw" + "\n")


def process_line(line):
    s = set(line)
    if s == set('XT') or s == set('X'):
        return "X won"
    if s == set("OT") or s == set("O"):
        return "O won"
    return ""

if __name__ == '__main__':
    file_in = open(sys.argv[1])
    file_out = open(sys.argv[2], 'w')
    process_input(file_in, file_out)
    file_in.close()
    file_out.close()
