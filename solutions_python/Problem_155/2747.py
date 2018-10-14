__author__ = 'Rachel&Stephane'
__file__ = 'StandingOvation'


def count_public_to_had(s_max, s_public):
    public_standing = 0
    public_to_had = 0
    for c in xrange(s_max+1):
        if public_standing < c:
            public_to_had += 1
            public_standing += 1
        public_standing += int(s_public[c])
    return public_to_had


def main():
    test_file = raw_input("> ")
    if test_file == "test":
        name_file_in = "test.in"
    else:
        letter = test_file[0]
        if test_file[1] == "s":
            name_file_in = letter + "-small-attempt0.in"
        else:
            name_file_in = letter + "-large.in"

    file_in = open(name_file_in, "r")
    name_file_out = name_file_in[:-2] + "out"
    file_out = open(name_file_out, "w")

    nb_cases = int(file_in.readline().rstrip('\n\r'))
    for case in xrange(nb_cases):
        s_max, s_public = file_in.readline().rstrip('\n\r').split()
        public_to_had = count_public_to_had(int(s_max), s_public)
        file_out.write("Case #" + str(case + 1) + ": " + str(public_to_had) + "\n")

    file_in.close()
    file_out.close()


main()
