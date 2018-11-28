'''
Created on 2012-4-14

@author: Philip85517
'''

input_file='B-large.in'
#input_file='small.in'
output_file='big.out'
file_handle = open(input_file, "r")
output_handle = open(output_file, "w")
T = int(file_handle.readline())
surprise = [[-1 for i in range(0, 2)] for i in range(0, 31)]

for i in range(0, 11):
    for j in range(0, 11):
        for k in range(0, 11):
            val_min = min(i, j, k)
            val_max = max(i, j, k)
            if val_max - val_min == 2:
                surprise[i + j + k][0] = max(surprise[i + j + k][0], val_max)
            elif val_max - val_min < 2:
                surprise[i + j + k][1] = max(surprise[i + j + k][1], val_max)

for i in range (0, T):
    line = map(int, file_handle.readline().split())
    Num = line[0]
    S = line[1]
    P = line[2]
    score = line[3:]
    
    F = [[0 for k in range(0, Num + 1)] for k in range(0, Num + 1)];
    
    for m in range(0, Num):
        for n in range(0, S + 1): 
            if surprise[score[m]][1] != -1:
                F[m + 1][n] = max(F[m + 1][n], F[m][n] + int(surprise[score[m]][1] >= P))
            if n > 0 and surprise[score[m]][0] != -1:
                F[m + 1][n] = max(F[m + 1][n], F[m][n - 1] + int(surprise[score[m]][0] >= P))
    
    print >> output_handle, "Case #%d: %d" % (i + 1, F[Num][S])

output_handle.close()