import sys

phrase = "welcome to code jam"
file = open(sys.argv[1])
out = open('c.out', 'w')

num = int(file.readline())
lineNum = 1
for line in file:
    mat = [[0 for j in range(len(phrase)+1)] for i in range(len(line)+1)]
    # initialize
    for i in range(0, len(mat)):
        mat[i][0] = 1
    # fill out dp matrix
    for i in range(1, len(mat)): #length of line
        for j in range(1, len(mat[i])): # length of 'wel to jam'
            if line[i-1] == phrase[j-1]:
                mat[i][j] = mat[i-1][j-1] + mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]
    ans = str(mat[-1][-1]%10000)
    if len(ans) < 4:
        for i in range(4-len(ans)):
            ans = '0' + ans
    out.write('Case #' + str(lineNum) + ': ' + str(ans) + '\n')
    lineNum = lineNum + 1
