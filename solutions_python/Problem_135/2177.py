import argparse

def to_int(string):
    return [int(x) for x in string.split()]

def process_input(filename):
    with open(filename, 'r') as infile:
        T = int(infile.next())
        for i in range(1,T+1):
            row = int(infile.next())
            for j in range(1,5):
                if j == row:
                    first_match = to_int(infile.next())
                else: infile.next()
            row2 = int(infile.next())
            for j in range(1,5):
                if j == row2:
                    second_match = to_int(infile.next())
                else: infile.next()
            overlap = list(filter(lambda x: x in second_match, first_match))


            cheated = -2
            bad_magician = -1
            if len(overlap) == 0:
                write_output(cheated,i)
            elif len(overlap) > 1:
                write_output(bad_magician, i)
            else:
                write_output(overlap[0],i)
            

def write_output(output, t):
    message = output
    if message == -1:
        message = 'Bad magician!'
    elif message == -2:
        message = 'Volunteer cheated!'
    print ("Case #{0}: {1}".format(t, message))


#==============================
# Copy below for future programs
#===============================

def main():
    args = arg_parse()
    process_input(args.input_file)


def arg_parse():
    parser = argparse.ArgumentParser(description='Solve the 2014 Google Code Jam Magic Trick problem')
    parser.add_argument('input_file', metavar='file')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
