def cake(r, c, cake_mat):
    for i in xrange(r):
        if cake_mat[i].count('?') < c:
            last_row = i
            break
    for i in xrange(last_row, -1, -1):
        cake_mat[i] = cake_mat[last_row]
    for i in xrange(last_row, r):
        if cake_mat[i].count('?') == c:
            cake_mat[i] = cake_mat[last_row]
            continue
        for j in xrange(c):
            if cake_mat[i][j] != '?':
                last_row = i
                break
        cake_mat[i][:j] = [cake_mat[i][j]]*j
        last_c = cake_mat[i][j]
        for j in xrange(j+1, c):
            if cake_mat[i][j] != '?':
                last_c = cake_mat[i][j]
                continue
            cake_mat[i][j] = last_c
    for i in xrange(r):
        assert not '?' in cake_mat[i]

def main(fname):
    in_fd = open(fname, "rb")
    out_fd = open(fname + ".out", "wb")
    t = int(in_fd.readline().strip())
    for i in xrange(t):
        r, c = map(int, in_fd.readline().strip().split(" "))
        cake_mat = []
        for j in xrange(r):
            cake_mat.append(list(in_fd.readline().strip()))
        out_fd.write("Case #%d:\n" % (i+1))
        cake(r, c, cake_mat)
        for j in xrange(r):
            out_fd.write("".join(cake_mat[j]) + "\n")
    in_fd.close()
    out_fd.close()
