def out(cn, smax, s, f):
    if len(s) == 0:
        f.write("Case #" + str(cn) + ": 0\n")
    else:
        r = 0
        total = int(s[0])
        for i in range(1, len(s)):
            si = int(s[i])
            if i > total:
                if r < i-total:
                    r = i - total
            total = total + si
        f.write("Case #" + str(cn) + ": " + str(r)+"\n")

def run():
    #in_file = "in1.txt"
    in_file = "A-large.in"
    out_file = "out1.txt"
    in_f  = open(in_file, 'r')
    out_f = open(out_file, 'w')

    T = int(in_f.readline())
    for i in range(1,T+1):

        smax, s = in_f.readline().strip().split()
        #s = in_f.readline().strip()
        out(i, smax, s, out_f)
    in_f.close()
    out_f.close()

if __name__ == "__main__":
    run()