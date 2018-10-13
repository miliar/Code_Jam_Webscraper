def search_next(stri, lt, stri_index, lt_pos):
    found = []
    sum = 0

    idx = stri.find(lt[lt_pos], stri_index)
    # element not found - unable to build a sentence
    if idx == -1: return 0

    while idx != -1:
        found.append(idx)
        idx = stri.find(lt[lt_pos], idx+1)

    # last element, found at least one
    if lt_pos == len(lt)-1: return len(found)

    for p in found:
        sum += search_next(stri, lt, p+1, lt_pos+1)
    return sum



if __name__ == '__main__':
    fin = open("./test.in", "r")
    fout = open("./test.out", "w")

    line = fin.readline()
    N = int(line)

    for test in range(0, N):
        txt = fin.readline().replace("\n", "")
        total = 0

        ltrs = ['w', 'e', 'l', 'c', 'o', 'm', 'e', ' ',
                't', 'o', ' ',
                'c', 'o', 'd', 'e', ' ',
                'j', 'a', 'm' ]

        total = search_next(txt, ltrs, 0, 0)

        fout.write("Case #" + str(test+1) + ": " + str(total).zfill(4) + "\n")