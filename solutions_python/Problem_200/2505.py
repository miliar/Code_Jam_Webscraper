filepath = '''C:\\Users\\ChutMap\\Downloads\\B-large.in'''
with open(filepath) as file:
    lines_in_file = file.readlines()
pos_in_lines = 0

def nextline():
    global pos_in_lines
    s = lines_in_file[pos_in_lines]
    pos_in_lines += 1
    return s.strip()

def solve_case():
    line_of_number = nextline()
    list_number = list(line_of_number)

    for n in range(len(list_number)):
        for i in range(len(list_number) - 1):
            if list_number[i] > list_number[i + 1]:
                list_number[i] = str(int(list_number[i]) - 1)
                for j in range(i + 1, len(list_number)):
                    list_number[j] = '9'
    return int(''.join(list_number))


n = int(nextline())

with open('''C:\\Users\\ChutMap\\Downloads\\output_tidynumber.txt''', 'w') as file:
    for i in range(1, n+1):
        res = solve_case()
        print("Case #%s: %s" % (i, res))
        print("Case #%s: %s" % (i, res), file=file)
