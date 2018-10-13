

def find_last_tidy_number(N):
    """
    N is either a integer or a string representing a number.
    Finds the lastest tidy number
    """
    N = int(N)
    for i in xrange(N, -1, -1):
        if str(i) == "".join(sorted([c for c in str(i)])):
            return i


FILE = "B-small-attempt1.in"
INPUT = open(FILE, 'r')
OUTPUT = open(FILE + "-OUT", 'w')

C = int(INPUT.readline())
for j in xrange(1, C + 1):
    answer = "Case #{}: {}\n".format(
        j, find_last_tidy_number(INPUT.readline()))
    OUTPUT.write(answer)
