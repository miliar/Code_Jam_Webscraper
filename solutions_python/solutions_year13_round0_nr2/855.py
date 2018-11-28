def solve(case_id, lawn, N, M, out):
    if N <= 1 or M <=1:
        out.write("Case #" + str(case_id) + ": YES\n")
        return

    for i in range(0,N):
        for j in range(0,M):
            h = lawn[i][j]
            #check if there is a larger height above:
            for l in range(0,i):
                if (lawn[l][j] > h):
                    break
            else:
                #check if there is a larger height below:
                for l in range(i+1,N):
                    if (lawn[l][j] > h):
                        break
                else:
                    continue
            
            #check if there is a larger height on the left:
            for c in range(0,j):
                if (lawn[i][c] > h):
                    break
            else:
                #check if there is a larger height on the right:
                for c in range(j+1,M):
                    if (lawn[i][c] > h):
                        break
                else:
                    continue
            out.write("Case #" + str(case_id) + ": NO\n")
            return
    out.write("Case #" + str(case_id) + ": YES\n")


input_file = 'B-large.in'
output_file = 'output.txt'

f = open(input_file, 'r')
out = open(output_file, 'w')

#read no test cases:
no_tests = int(f.readline())

for test in range(0, no_tests):
    line = f.readline()
    l = line.split()
    N = int(l[0])
    M = int(l[1])
    #read lawn pattern:
    lawn = []
    for i in range(0, N):
        line = f.readline()
        row = [int(x) for x in line.split()]
        lawn.append(row)
    solve(test+1, lawn, N, M, out)
    
f.close()
out.close()
