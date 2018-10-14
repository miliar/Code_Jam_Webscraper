
fin = open ('c:/users/hai/my projects/google code jam/2011/qualification/D/D-large.in')
fout = open ('c:/users/hai/my projects/google code jam/2011/qualification/D/D-large.out','w')
T = int(fin.readline())
for testcase in range(1,T+1):
    fin.readline()
    array = [int(x) for x in fin.readline().split()]
    sorted_array = list(sorted(array))
    count_unsorted = 0
    for i in range(len(array)):
        if array[i] != sorted_array[i]:
            count_unsorted +=1
    fout.write ('Case #' + str(testcase) + ': ' + str(count_unsorted) + '\n')
fin.close()
fout.close()
