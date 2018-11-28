def main():
    f_in = open("A-small-attempt1.in", "r")
    f_out = open("output.txt", "w")

    t = int(f_in.readline())
    for tt in xrange(t):
        print "*" *10
        invite_count = 0
        line = f_in.readline().strip().split()
        smax = int(line[0])
        s = line[1]
        cur_count = int(s[0])
        for i in range(1, len(s)):
            si = int(s[i])
            if si == 0: continue
            if cur_count < i:
                invite_count += (i-cur_count)
                cur_count += si + invite_count
            else:
                cur_count += si

            print "i={} cur_count={} invite_count={}\n".format(i, cur_count, invite_count)


        f_out.write("Case #{}: {}\n".format(tt+1, invite_count))

    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
