def read_int_line(f):
    return int(f.readline().replace("\n",""))

def read_int_arr(f):
    return map(int, f.readline().replace("\n","").split(" "))

def main(inf, outf):
    fr = open(inf)
    fw = open(outf, 'w')
    T = read_int_line(fr)
    for i in range(T):
        N, K = read_int_arr(fr)
        #print "\n-----------\nCase #%d" % (i + 1)
        res = "Case #%d: %s\n" % (i+1, "ON" if result(N,K) else "OFF")
        fw.write(res)
    fw.close()
    fr.close()

def result(N, K):
    snappers = [[False, False] for a in range(N)]
    snappers[0][0] = True
    snappers = tuple(snappers)
    for i in range(K):
        #print "Click #%d\nInit: \t\t\t\t" % (i+1), snappers
        for snapper in [snap for snap in snappers if snap[0]]:
            snapper[1] = not snapper[1]
        #print "After Switching: \t", snappers

        snapper_before = snappers[0]
        for snapper in snappers[1:]:
            snapper[0] = sum(snapper_before) == 2
            snapper_before = snapper
        #print "After Power: \t\t", snappers

    for snapper in snappers:
        if sum(snapper) != 2:
            return False

    return True

if __name__ == "__main__":
    main('A-small-attempt0.in', 'snapper.out')