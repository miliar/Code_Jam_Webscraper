"""
    Oh yeah
"""

def tidify(num):
    num_list = list(str(num))
    num_list = map(lambda x : int(x), num_list)
    for i in range(len(num_list)-1, 0, -1):
        if num_list[i-1] > num_list[i]:
            num_list[i-1] -=1
            for j in range(i, len(num_list)):
                num_list[j] = 9
    num_list = map(lambda x : str(x), num_list)
    s_num = ''.join(num_list)
    return int(s_num)

def count_tidy(N):
    return tidify(N)

with open('B-large.in') as file:
    with open('output.raw' ,'w') as ofile:
        n = int(file.readline())
        i = 1
        for line in file:
            ofile.write('Case #{}: {}\n'.format(i, count_tidy(int(line))))
            i += 1
