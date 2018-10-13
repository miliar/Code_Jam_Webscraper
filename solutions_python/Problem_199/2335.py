filepath = '''C:\\Users\\ChutMap\\Downloads\\A-large.in'''
with open(filepath) as file:
    lines_in_file = file.readlines()
pos_in_lines = 0

def nextline():
    global pos_in_lines
    s = lines_in_file[pos_in_lines]
    pos_in_lines += 1
    return s.strip()

def solve_case():
    """
    ---+-++- 3
    """
    pancakes, pancake_per_flip = nextline().split()
    pancakes = list(pancakes)
    pancake_per_flip = int(pancake_per_flip)
    num_flips = 0

    for i in range(len(pancakes) - pancake_per_flip + 1):
        if pancakes[i] == "-":
            num_flips += 1
            for j in range(i, i + pancake_per_flip):
                if pancakes[j] == "+":
                    pancakes[j] = "-"
                else:
                    pancakes[j] = "+"

    if pancakes == list("+"*len(pancakes)):
        return num_flips
    else:
        return "IMPOSSIBLE"


n = int(nextline())

with open('''C:\\Users\\ChutMap\\Downloads\\output1.txt''', 'w') as file:
    for i in range(1, n+1):
        res = solve_case()
        print("Case #%s: %s" % (i, res))
        print("Case #%s: %s" % (i, res), file=file)
