# Codejam 2017 - Qualification Round
# Problem B: Tidy Numbers
# Author: Andy Zhou

# Could optimise further: only need to check two choices really per digit sort of
def find_highest(roof:int):
    length = len(str(roof))
    if int('1' * length) > roof:  # best is a digit less
        return int('9' * (length - 1))
    result = []
    for index in range(length):
        curr = int(''.join(result)) * 10 ** (length - index) if len(result) else 0
        lowest = int(result[-1]) if len(result) else 1
        for x in range(9, lowest - 1, -1):
            # determine the next digit
            remainder = int(str(x) * (length - index))
            if curr + remainder <= roof:
                result.append(str(x))
                break
    return int(''.join(result))

fin = open("B-large.in", "r")
fout = open("b-out.txt", "w")
num_cases = int(fin.readline())
for case in range(1, num_cases + 1):
    upper = int(fin.readline())
    answer = find_highest(upper)
    fout.write("Case #{}: {}\n".format(case, answer))
fin.close()
fout.close()
