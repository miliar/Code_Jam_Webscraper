def readint(file):
    return int(file.readline().strip())

def num_to_list(num):
    ret = []
    if num == 0:
        return [0]
    while (num):
        ret = [num % 10] + ret
        num = int(num // 10)
    return ret

def list_to_num(l):
    ret = 0
    for i in l:
        ret = ret * 10 + i
    return ret

with open("B-large.in") as ifile:
    with open("output_tidy.txt", "w") as ofile:
        T = readint(ifile)
        for i in range(T):
            N = readint(ifile)
            list_N = num_to_list(N)
            idx = 0
            while idx < (len(list_N) - 1):
                if list_N[idx + 1] < list_N[idx]:
                    for ii in range(idx + 1, len(list_N)):
                        list_N[ii] = 9
                    list_N[idx] -= 1
                    while idx > 0 and list_N[idx - 1] > list_N[idx]:
                        list_N[idx] = 9
                        list_N[idx - 1] -= 1
                        idx -= 1
                    break
                else:
                    idx += 1
            if list_N[0] == 0:
                list_N.pop(0)
            ofile.write("Case #{}: {}\n".format(i+1, list_to_num(list_N)))

