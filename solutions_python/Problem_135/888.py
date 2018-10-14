from collections import deque
f = open('./A-small-attempt0.in')
nbrs = deque([int(k) for k in f.read().split()])
f.close()

def r():
    return nbrs.popleft()

def extract_row():
    selected = r()
    rows = [[0 for i in range(0, 4)] for j in range(0, 4)]
    for i in range(0, 4):
        for j in range(0, 4):
            rows[i][j] = r()
    return rows[selected-1]

f = open('output.out', 'w')
cases = r()
for current_case in range(0, cases):
    A = extract_row()
    B = extract_row()
    C = list(set(A).intersection(B))
    f.write('Case #' + str(current_case+1) + ': ')
    if len(C) == 0:
        f.write('Volunteer cheated!\n')
    elif len(C) == 1:
        f.write(str(C[0]) + '\n')
    else:
        f.write('Bad magician!\n')

f.close()