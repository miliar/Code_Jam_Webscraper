"""
returns the last tidy number
ie number whose digits left to right are non decreasing
"""

# read in
inList = []
fname_in = "B-small-attempt3.in"
with open(fname_in, "r") as infile:
    for line in infile:
        inList.append(line.strip().split(" "))

total_cases = int(inList[0][0])
index = 1

def tidy_test(n):
    """ checks that n is tidy """
    n_str = str(n)
    n_len = len(n_str)
    tidy = True

    for i in range(n_len-1):
        if n_str[i] > n_str[i+1]:
            tidy = False
    return tidy


def tidy(n):
    while True:
        if tidy_test(n):
            return n
        n -= 1

# prepare to write out
outList = []
while index <= total_cases:
    n = int(inList[index][0])
    outList.append(tidy(n))
    index += 1

# write out
fname_out = "tidy-output-small.out"
with open(fname_out, "w") as outfile:
    case_no = 1
    for n in outList:
        outfile.write("Case #{}: {}".format(case_no, n) + "\n")
        case_no += 1
