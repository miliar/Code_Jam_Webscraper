import sys

FAIL_FILE = "failed.in"
OUT_FILE = "output"

def parse_input(fd, testcase_callback):
    failed = []
    nb_testcases = int(fd.readline())
    with open(OUT_FILE, "w") as out_fd:
        for i in xrange(0, nb_testcases):
            line = fd.readline().strip()
            args = line.split(" ")

            if not testcase_callback(i + 1, args, out_fd):
                failed.append(args)
    with open(FAIL_FILE, "w") as fail_fd:
        fail_fd.write(str(len(failed)) + "\n")
        for args in failed:
            fail_fd.write(" ".join(args) + "\n")

def testcase(case_number, args, out_fd):
    try:
        print "args = %s" % (args,)

        Smax = int(args[0])
        audience = []
        for i in args[1]:
            audience.append(int(i))

        res = do_it(Smax, audience)

        print "Case #%d: %d" % (case_number, res)
        out_fd.write("Case #%d: %d\n" % (case_number, res))

        return True
    except Exception as ex:
        print ex
        exit()
    return False

def do_it(Smax, audience):
    missing = 0
    current = 0
    for needed in xrange(len(audience)):
        stand_up = audience[needed]
        if needed > current + missing:
            missing += 1
        current += stand_up

    return missing

parse_input(sys.stdin, testcase)
