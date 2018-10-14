filename = "B-large.in"
input_file = open(filename, 'r')
N = 0
M = 0
lawn = []

def get_lawn():
    lawn = []
    for i in range(N):
        line = input_file.readline().split(' ')
        row = []
        for e in line:
            row.append(int(e))
        lawn.append(row)
    return lawn

def is_row_impossible(i, j):
    for e in lawn[i]:
        if e > lawn[i][j]:
            return True
    return False

def is_col_impossible(i, j):
    for p in range(N):
        if lawn[p][j] > lawn[i][j]:
            return True
    return False

def is_impossible(i, j):
    if is_row_impossible(i, j) and is_col_impossible(i, j):
        return True
    else:
        return False

def judgement(N, M):
    for i in range(N):
        for j in range(M):
            if is_impossible(i, j):
                print "Case #" + str(c+1) + ": NO"
                return
    print "Case #" + str(c+1) + ": YES"

case = input_file.readline()
for c in range(int(case)):
    size = input_file.readline().split(' ')
    N = int(size[0])
    M = int(size[1])
    lawn = get_lawn()
    judgement(N, M)

input_file.close()
