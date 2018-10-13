

fin = open("B-small-attempt2.in", "r")
# fin = open("B-large-practice.in", "r")
fout = open("B-small-attempt2.out", "w")
# fout = open("B-large-practice.out", "w")

def is_smaller(list):
    pivot = list[1]
    is_ok = True
    d = list[2:]
    for el in d:
        if pivot > el:
            is_ok = False
            break
    return is_ok


testcases = fin.readline()
for index, line in enumerate(fin.readlines()):
    line = int(line.rstrip("\n"))
    if line <= 9:
        fout.write("Case #{0}: {1}\n".format(index+1, line))
    else:
        is_correct = False
        while True:
            line = int(line)
            if line <= 9:
                fout.write("Case #{0}: {1}\n".format(index+1, line))
                break
            digs = map(int, str(line))
            for ind, dig in enumerate(reversed(digs)):
                i = -ind-1
                i_prev = -ind -2
                if ind == len(digs) - 1:
                    if digs[0] != 0 and digs[0] <= digs[1] and is_smaller(digs):
                        is_correct = True
                    elif digs[0] == 0:
                        digs = list((len(digs)-1)*"9")
                        is_correct = True
                    elif digs[0] > digs[1] or not is_smaller(digs):
                        for i in range(1, len(digs)):
                            digs[i] = 9
                        is_correct = True
                    break

                    # if is_ok:
                    #     is_correct = True
                    #     break
                    # else:
                    #     break
                elif dig < digs[i_prev]:
                    digs[i] = 9
                    digs[i_prev] = digs[i_prev] - 1
            if is_correct:
                output = int(''.join(map(str,digs)))
                fout.write("Case #{0}: {1}\n".format(index+1, output))
                break

fin.close()
fout.close()

