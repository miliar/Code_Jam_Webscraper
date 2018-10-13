import sys

OUT_FILE = "output"

def get_solutions():
    cols1 = 4
    rows1 = 4
    Xomino1 = 4

    solutions = {}
    for cols in xrange(1, max(cols1, rows1) + 1):
        solutions[cols] = {}
        for rows in xrange(1, max(cols1, rows1) + 1):
            solutions[cols][rows] = {}
            for Xomino in xrange(1, Xomino1 + 1):
                solutions[cols][rows][Xomino] = None


    print "X C R"
    count = 0
    for cols in xrange(1, cols1 + 1):
        for rows in xrange(1, rows1 + 1):
            for Xomino in xrange(1, Xomino1 + 1):

                if solutions[cols][rows][Xomino] is not None:
                    res = solutions[cols][rows][Xomino]
                    print Xomino, rows, cols, res, "1"
                elif (rows * cols) % Xomino != 0:
                    #RICHARD
                    print Xomino, rows, cols, "RICHARD  2"
                    res = False
                elif Xomino > (rows * cols):
                    #RICHARD
                    print Xomino, rows, cols, "RICHARD  3"
                    res = False
                elif Xomino > 6:
                    #RICHARD
                    print Xomino, rows, cols, "RICHARD  4"
                    res = False
                elif Xomino > rows and Xomino  > cols:
                    #RICHARD
                    print Xomino, rows, cols, "RICHARD  5"
                    res = False
                elif Xomino == 1:
                    #GABRIEL
                    print Xomino, rows, cols, "GABRIEL  6"
                    res = True
                elif Xomino == 2:
                    #GABRIEL
                    print Xomino, rows, cols, "GABRIEL  7"
                    res = True
                elif Xomino == 3 and (rows * cols) % 2 == 0 and (rows * cols) >= 6:
                    #GABRIEL
                    print Xomino, rows, cols, "GABRIEL  8"
                    res = True
                elif (rows <= ((Xomino - 1) / 2) or cols <= ((Xomino - 1) / 2)):
                    #RICHARD
                    print Xomino, rows, cols, "RICHARD  9"
                    res = False
                elif Xomino == 3 and (rows % Xomino == 0 or cols % Xomino == 0):
                    #GABRIEL
                    print Xomino, rows, cols, "GABRIEL 10"
                    res = True
                elif Xomino == 4 and (rows == 2 or cols == 2):
                    print Xomino, rows, cols, "RICHARD 11"
                    res = False
                elif Xomino == 4 and ((rows == 4 and cols in (3, 4)) or (rows == (3, 4) and cols == 4)):
                    print Xomino, rows, cols, "GABRIEL 12"
                    res = True
                else:
                    res = None
                    count += 1

                solutions[cols][rows][Xomino] = res
                solutions[rows][cols][Xomino] = res

                if res is None:
                    print Xomino, rows, cols, "<============"
                elif res:
                    #print Xomino, rows, cols, "GABRIEL"
                    pass
                else:
                    #print Xomino, rows, cols, "RICHARD"
                    pass

    print count
    return solutions



def parse_input(fd):
    nb_testcases = int(fd.readline())
    with open(OUT_FILE, "w") as out_fd:
        for case_number in xrange(0, nb_testcases):
            line = fd.readline().strip()

            args = line.split(" ")
            Xomino = int(args[0])
            cols = int(args[1])
            rows = int(args[2])

            solutions = get_solutions()
            res = solutions[cols][rows][Xomino]
            if not res:
                print "Case #%d: %s" % (case_number + 1, "RICHARD")
                out_fd.write("Case #%d: %s\n" % (case_number + 1, "RICHARD"))
            else:
                print "Case #%d: %s" % (case_number + 1, "GABRIEL")
                out_fd.write("Case #%d: %s\n" % (case_number + 1, "GABRIEL"))



parse_input(sys.stdin)
