def read_int_line(f):
    return int(f.readline().replace("\n",""))

def read_int_arr(f):
    return map(int, f.readline().replace("\n","").split(" "))

def main(inf, outf):
    fr = open(inf)
    fw = open(outf, 'w')
    T = read_int_line(fr)
    for i in range(T):
        R, k, N = read_int_arr(fr)
        G = read_int_arr(fr)
        res = "Case #%d: %d\n" % (i+1, result(R,k,N,G))
        fw.write(res)
    fw.close()
    fr.close()

def result(R,k,N,groups):
    #R - times can go
    #k - people can hold at once
    #N - number of groups
    sum = 0
    for r in range(R):
        total_this_turn = 0
        groups_this_turn = []
        while True:
            #Is next group fits
            if not groups:
                sum += total_this_turn
                break
            s = total_this_turn + groups[0]
            if k >= s:
                total_this_turn = s
                groups_this_turn.append(groups.pop(0))
            else:
                sum += total_this_turn
                break
        groups.extend(groups_this_turn)
    return sum

if __name__ == "__main__":
    main('C-small-attempt0.in', 'roller.out')