#
# Aldo Mendoza
# Google Code Jam
#   Qualification Round 2014
# aldus.91@gmail.com
#

#
# Function that reads a square arrangement
#
def read_arrangement(length):
    arrangement = []

    for _ in range(length):
        line = raw_input().split(' ')
        arrangement.append(line)

    return arrangement

#
# Process a single case and returns a string with the result
#
def process_case():
    first_answer = int(raw_input())
    first_arrangement = read_arrangement(4)

    second_answer = int(raw_input())
    second_arrangement = read_arrangement(4)

    first_row = set(first_arrangement[first_answer - 1])
    second_row = set(second_arrangement[second_answer - 1])

    common = first_row.intersection(second_row)

    if (len(common) == 0):
        return 'Volunteer cheated!'
    elif (len(common) == 1):
        return common.pop()
    else:
        return 'Bad magician!'

#
# Entry point
#
T = int(raw_input())

for case in range(1, T + 1):
    print "Case #%d: %s" % (case, process_case())
