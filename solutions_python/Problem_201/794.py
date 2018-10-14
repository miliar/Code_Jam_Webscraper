import sys
from collections import defaultdict

def main():

    #  reading in the arguments of the code executable
    fin_name = sys.argv[1]
    fout_name = sys.argv[2]

    # opening the output file for writing
    fout = open(fout_name, 'w')

    #  reading all lines at once from the opened file
    with open(fin_name, 'r') as fin:
        lines = fin.readlines()

    # T - number of test casess
    T = int(lines[0].split()[0])

    for test_case in range(1, T+1):

        stalls, people = [int(x) for x in lines[test_case].split()]

        max_S, min_S = find_stalls_distance_last(stalls, people)
        output_string = str(max_S) + " " + str(min_S)

        fout.write("Case #"+str(test_case)+": "+output_string+"\n")

    fin.close()
    fout.close()


def find_stalls_distance_last(stalls, people):


    #  if only one person, just return right/left count of the stalls
    if people == 1:
        return [stalls//2, (stalls-1)//2]

    #  introduce the first placement of the person (here denoted as "division")
    parts = defaultdict(int)

    parts[stalls//2] += 1
    parts[(stalls-1)//2] += 1

    divisions = 1

    # check if by another division of each subinterval into two smaller subintervals
    #  yields more or the same amount of people than requested and make divisions
    #  counting the number of subintervals of certain length

    while 2*divisions + 1 < people:

        new_parts = defaultdict(int)
        divisions = 2*divisions + 1
        for part in parts:
            new_parts[part//2] += parts[part]

            if part != 0:
                new_parts[(part-1)//2] += parts[part]

        parts = new_parts



    #  sort for checking first the largest intervals
    all_parts_counts = [[key, parts[key]] for key in sorted(parts, reverse=True)]

    # if parts found for placement of additional people is still small, continue
    #  with smaller parts
    parts_found = divisions
    it = -1
    while parts_found < people:
        it += 1
        parts_found += all_parts_counts[it][1]

    # finally the interal where our last person will be is found, so lets return
    #  the right and left number of stalls when placing the person there
    part_size = all_parts_counts[it][0]

    return [part_size//2, max(0,(part_size-1)//2)]


if __name__ == "__main__":
    main()
