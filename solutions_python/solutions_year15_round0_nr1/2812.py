def f(s,c):
    friend_num = 0
    guest_nums = 0
    for i in xrange(c+1):
        n = int(s[i])
        if guest_nums >= i:
            guest_nums += n
        elif n == 0:
            pass
        else:
            friend_num += i - guest_nums
            guest_nums = n + i
    return friend_num

def main(file):
    outfile = open("utdata.txt", "w")
    with open(file, "r") as infile:
        infile.readline()
        for i, line in enumerate(infile):
            a, b = line.split()
            outfile.write("Case #%d: %d\n" % (i+1, f(b, int(a))))
    outfile.close()

main("A-large.in")