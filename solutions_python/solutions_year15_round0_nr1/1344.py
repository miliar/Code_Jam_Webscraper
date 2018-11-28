import sys


def opera(shyness):
    required_friends = 0
    currently_clapping = 0
    for level_shyness, level_population in enumerate(shyness):
        if currently_clapping < level_shyness:
            level_missing = level_shyness - currently_clapping
            required_friends += level_missing
            currently_clapping += level_missing
        currently_clapping += level_population
    return required_friends


def main(file_name):
    input_file = open(file_name, "r")
    out_file = open("%s.ans" % file_name, "w")
    cases = int(input_file.readline().strip())
    for i in range(cases):
        smax, si = input_file.readline().split(" ")
        smax = int(smax)
        si = map(int, si.strip())
        assert smax + 1 == len(si), "%d != len(%s)" % (smax + 1, si)
        out = opera(si)
        out_file.write("Case #%d: %d\n" % (i + 1, out))
    out_file.close()
    input_file.close()

if __name__ == "__main__":
   main(sys.argv[1])
