# Google Code Jam 2014 Qualification Round
# Problem D
# Shaotong Wang

# Find the least element in sorted [iterable] greater than [n]
def find_least_greater(n, iterable):
    for x in iterable:
        if x > n:
            return x
    return None
        

fin = open('D_test.in', 'r')
fout = open('D_test.out', 'w')

num_cases = int(fin.readline())

for case in range(1,num_cases+1):
    num_blocks = int(fin.readline())
    naomi_blocks = map(float, fin.readline().split())
    ken_blocks = map(float, fin.readline().split())
    naomi_blocks.sort()
    ken_blocks.sort()

    naomi_dwar, ken_dwar = naomi_blocks[:], ken_blocks[:]
    naomi_pt = 0
    for i in xrange(num_blocks):
        if naomi_dwar[0] < ken_dwar[0]:
            naomi_dwar.remove(naomi_dwar[0])
            ken_dwar.remove(ken_dwar[-1])
        else:
            naomi_pt += 1
            naomi_dwar.remove(naomi_dwar[0])
            ken_dwar.remove(ken_dwar[0])

    fout.write("Case #" + str(case) + ": " + str(naomi_pt) + " ")

    naomi_pt = 0
    for i in xrange(num_blocks):
        n = find_least_greater(naomi_blocks[i], ken_blocks)
        if n == None:
            naomi_pt += 1
            ken_blocks.remove(ken_blocks[0])
        else:
            ken_blocks.remove(n)

    fout.write(str(naomi_pt) + "\n")

fin.close()
fout.close()
