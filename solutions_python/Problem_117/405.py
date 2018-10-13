in_data = open('B-large.in').readlines()
in_data = [x.strip() for x in in_data]
T = int(in_data[0])
in_data = in_data[1:]
res = open('result', 'w')

def test_lawn(lawn, colmax, rowmax, m, n, case_no):
    for i in range(n):
        for j in range(m):
            if lawn[i][j] < rowmax[i] and lawn[i][j] < colmax[j]:
                output = 'Case #' + str(case_no+1) + ': ' + 'NO' + '\n'
                return(output)
            
    output = 'Case #' + str(case_no+1) + ': ' + 'YES' + '\n'
    return(output)

for case_no in range(T):
    n, m = [int(x) for x in in_data[0].split()]
    dt = in_data[1:(n+1)]
    in_data = in_data[(n+1):]
    lawn = []
    for line in dt:
        line = [int(x) for x in line.split()]
        lawn.append(line)
    colmax = []
    for i in range(m):
        tmpcol = [lawn[x][i] for x in range(n)]
        colmax.append(max(tmpcol))
    rowmax = []
    for i in range(n):
        tmprow = lawn[i]
        rowmax.append(max(tmprow))
        
    output = test_lawn(lawn, colmax, rowmax, m, n, case_no)
    res.write(output)
    