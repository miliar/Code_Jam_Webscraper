def print_2d(tab):
    for e in tab:
        print(e)

def zlicz(num, cmp):
    ret = []
    for el in str(num):
        if(int(el) not in cmp):
            ret.append(-1)
            break
        if(int(el) != 0): ret.append(int(el))
    ret.sort()
    return ret

if __name__ == '__main__':
    fin = open("./test.in", "r")
    fout = open("./test.out", "w")

    line = fin.readline()
    N = int(line)

    for test in range(0, N):
        total = 0
        num = int(fin.readline())

        tmp = num
        num_nz_asc = []
        num_asc = []

        for el in str(num):
            num_asc.append(int(el))
            if(int(el) != 0): num_nz_asc.append(int(el))

        num_asc.sort()
        num_nz_asc.sort()
        desc = num_nz_asc[:]
        desc.sort(reverse=True)
        desc2 = []

        for w in desc:
            desc2.append(str(w))

        if(num == int("".join(desc2))):
            tmp = str(num_nz_asc[0])
            for q in range(0, num_asc.count(0)+1):
                tmp += "0"
            j=0
            for t in num_nz_asc:
                if(j > 0):
                    tmp += str(num_nz_asc[j])
                j += 1
        else:
            while(1):
                tmp += 1
                r = zlicz(tmp, num_asc)
                if(r == num_nz_asc):
                    #print(r == num_nz_asc)
                    break

        total = tmp

        sol = "Case #" + str(test+1) + ": " + str(total) + "\n"
        print(sol)
        fout.write(sol)