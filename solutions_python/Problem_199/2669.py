# Google Codejam 2017 - Qualification Round
# Problem A - Oversized Pancake Flipper
# AUTHOR: Andy Zhou

# just flip from the left, seems good

fin = open("A-large.in", "r")
fout = open("a-out.txt", "w")
num_cases = int(fin.readline())
for case in range(1, num_cases + 1):
    pancakes, k = fin.readline().split()
    pancakes = list(pancakes)
    k = int(k)
    # plus = len(filter(lambda x: x == "+", pancakes))
    flips = 0
    for index in range(len(pancakes) - k + 1):
        # flip if unflipped, yo
        if pancakes[index] == "-":
            flips += 1
            for j in range(index, index + k):
                pancakes[j] = "-" if pancakes[j] == "+" else "+"
    # check for unflipped
    result = "IMPOSSIBLE" if sum(x == "-" for x in pancakes) else flips
    print("Case #{}: {}".format(case, result))
    fout.write("Case #{}: {}\n".format(case, result))
        
fin.close()
fout.close()
