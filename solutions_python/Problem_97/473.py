# Date:2012-04-14
# Author: Chika

def cal_recycled_number(n, m):
    n = str(n)
    recycled_numbers = []
    for i in range(len(n)-1):
        recycled_number = n[(i+1):]+n[:(i+1)]
        if (recycled_number > n) and (int(recycled_number) <= m) and (recycled_number not in recycled_numbers) and (recycled_number[0] != '0'):
            recycled_numbers.append(recycled_number)
    return len(recycled_numbers)


with open("C-large.in") as infile:
    T = int(infile.readline())

    with open("C-large.out", "w") as outfile:
        for i in range(T):
            A, B = infile.readline().split()
            A = int(A)
            B = int(B)
            ret = 0
            if B <= 10:
                pass
            else:
                for j in range(A, B):
                    ret += cal_recycled_number(j, B)

            outfile.write("Case #%d: %d\n" % (i+1, ret, ))
