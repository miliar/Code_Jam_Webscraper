


def check_feasibility(S):
    row_vals = []
    col_vals = []
    for row in S:
        row_vals.append(max(row))
    for c in range(len(S[0])):
        col = []
        for row in S:
            col.append(row[c])
        col_vals.append(max(col))

    for rc in range(len(S)):
        for cc in range(len(S[0])):
            if (SQ[rc][cc] != min([row_vals[rc], col_vals[cc]])):
                return "NO"
    return "YES"




fid_ip = open('B-large.in', 'r')
fid_op = open('output.in', 'w')

num_cases = int(fid_ip.readline())
for case in range(num_cases):
    [N, M] = [int(x) for x in fid_ip.readline().split()]
    SQ = []
    for n in range(N):
      SQ.append([int(x) for x in fid_ip.readline().split()])

    fid_op.write('Case #' + str(case+1) + ': ' + check_feasibility(SQ) + '\n')

