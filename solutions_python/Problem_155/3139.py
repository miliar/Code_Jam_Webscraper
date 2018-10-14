import sys
from os.path import splitext


def minimum_friends_for_ovation(max_shyness, shynesses):
    friends = 0
    clappers = 0
    for shyness, count in enumerate(shynesses):
        if shyness > clappers + friends:
            # add enough friends so that these people will clap
            friends += shyness - clappers - friends

        # since they will clap, count them as clappers for the next group
        clappers += count
    return friends

if __name__ == "__main__":
    input_file = sys.argv[1]

    with open(input_file) as fin:
        # don't actually need this, but it's there:
        n_cases = int(fin.readline())

        # each line is a case number, so iterate through and solve
        with open(splitext(fin.name)[0]+'.out', 'w') as fout:
            for case, line in enumerate(fin):
                # extract the problem info. from the line
                # and format them nicely
                max_shyness, shynesses = line.split(' ')
                max_shyness = int(max_shyness)
                shynesses = [int(v) for v in list(shynesses)[:-1]]  # remove "\n"

                # write the answer to file
                fout.write("Case #{0}: {1}\n".format(
                    case+1,
                    minimum_friends_for_ovation(
                        int(max_shyness),
                        shynesses)))
