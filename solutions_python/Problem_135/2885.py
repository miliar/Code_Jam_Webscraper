filename = 'A-small.in'

f = open(filename, 'r')
num_cases = int(f.readline())

class Case:
    pass
    
def next_case(f):
    c = Case()
    c.ans1 = f.readline()
    if c.ans1 == '':
        return []
    c.ans1 = int(c.ans1)

    c.first_mat = []
    for i in range(4):
        c.first_mat.append(f.readline().split())

    c.ans2 = int(f.readline())
    c.second_mat = []
    for i in range(4):
        c.second_mat.append(f.readline().split())

    return c

c = next_case(f)
casenum = 1
while c != []:
    ans_row1 = c.first_mat[c.ans1 - 1]
    ans_row2 = c.second_mat[c.ans2 - 1]

    s1 = set(ans_row1)
    s2 = set(ans_row2)
    s3 = s1 & s2

    ans_str = 'Case #' + str(casenum) + ': '
    if len(s3) == 0:
        ans_str += 'Volunteer cheated!'
    elif len(s3) == 1:
        ans_str += s3.pop()
    elif len(s3) > 1:
        ans_str += 'Bad magician!'
    print(ans_str)

    c = next_case(f)
    casenum += 1

if casenum - 1 != num_cases:
    print('error: not all cases read')
f.close()
