import sys


def solve_m(m, sig):
    #print "sig: %s" % sig
    #print m
    num_columns = len(m[0])
    num_rows = len(m)
    moves = 0
    for i in range(num_columns):
        col_sum = 0
        for row in m:
            col_sum += row[i]

        avg = round(col_sum / num_rows)

        for row in m:
            #print "moves for %s %d - %d: %d" %(sig[i], row[i], avg, abs(row[i] - avg))
            moves += abs(row[i] - avg)

    return moves

def gen_sig(s):
    sig = s[0]
    chars = {s[0]: 1}
    count = 1
    counts = []
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            counts.append(count)
            sig += s[i]
            count = 1
        else:
            count += 1
    counts.append(count)
    return (sig, counts)


def solver(f):
    cases = int(f.readline().strip())
    for i in range(cases):
        num_strings = int(f.readline().strip())
        base_sig = None
        matrix = []
        strings = []
        res = "Case #%d: " % (i + 1)
        for i in range(num_strings):
            string = f.readline().strip()
            strings.append(string)
            (sig, chars) = gen_sig(string)
            if base_sig is None:
                base_sig = sig
            else:
                if sig != base_sig:
                    res += "Fegla Won"
                    print res

            matrix.append(chars)
        #print "%d %d" %(len(strings[0]), len(strings[1]))
        #print strings
        if base_sig == sig:
            #print "sig %s" % sig
            #print matrix
            num_moves = solve_m(matrix, sig)
            res += "%d" % num_moves
            print res

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        solver(f)

