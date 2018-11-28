
fin = open ('c:/users/hai/my projects/google code jam/2011/qualification/C/C-large.in')
fout = open ('c:/users/hai/my projects/google code jam/2011/qualification/C/C-large.out','w')

T = int(fin.readline())

for testcase in range(1,T+1):
    fin.readline()
    
    values = [int(x) for x in fin.readline().split()]

    xor_sum = 0
    for i in values:
        xor_sum ^= i

    if xor_sum == 0:
        # splitting possible
        best_split = sum(values) - min(values)
        outputline = 'Case #' + str(testcase)+': ' + str(best_split)
    else:
        # splitting impossible
        outputline = 'Case #' + str(testcase)+': ' + 'NO'

    fout.write (outputline+ '\n')
    
    


fin.close()
fout.close()
