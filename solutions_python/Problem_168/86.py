import os,sys

def check(F, r, c, dx, dy):
    R = len(F)
    C = len(F[0])

    #print "before check", r, c, dx, dy

    ch = False
    r = r + dy
    c = c + dx

    #print "start check", r, c, dx, dy, ch
    
    while r >= 0 and r < R and c >= 0 and c < C:
        #print "c",r,c,dx,dy
        if F[r][c] != '.':
            ch = True
            break
        r = r + dy
        c = c + dx

    #print "end check", r, c, ch

    return ch

DOWNLOADS = "C:\\Users\\vasiliy.strelnikov\\Downloads"

sel_files = []
for fname in os.listdir(DOWNLOADS):
	if fname[:2] == "A-" and fname[-3:] == ".in":
		print len(sel_files), ":", fname
		sel_files.append(fname)
len(sel_files) == 0 and sys.exit(0)

ix = int(sys.stdin.readline())

infile  = sel_files[ix]
outfile = infile[:-3] + ".out"

ifile = open(DOWNLOADS + "\\" + infile)
ofile = open(DOWNLOADS + "\\" + outfile, "w")

T = int(ifile.readline().strip())
for t in range(T):
    R, C = ifile.readline().strip().split()
    R, C = int(R), int(C)

    F = []
    for r in range(R):
        row = ifile.readline().strip()
        F.append(row)

    n = 0
    impossible = False

    for r in range(R):
        for c in range(C):
            if F[r][c] == '.':
                continue

            if F[r][c] == '>':
                need_change = not check(F, r, c, 1, 0)
                #print "Check",r,c,F[r][c],"need_change = ", need_change
                if need_change:
                    can_change = check(F, r, c, -1, 0) or check(F, r, c, 0, 1) or check(F, r, c, 0, -1)
                    if not can_change:
                        impossible = True
                        break;
                    else:
                        n = n + 1
            elif F[r][c] == '<':
                need_change = not check(F, r, c, -1, 0)
                #print "Check",r,c,F[r][c],"need_change = ", need_change
                if need_change:
                    can_change = check(F, r, c, 1, 0) or check(F, r, c, 0, 1) or check(F, r, c, 0, -1)
                    if not can_change:
                        impossible = True
                        break;
                    else:
                        n = n + 1
            elif F[r][c] == 'v':
                need_change = not check(F, r, c, 0, 1)
                #print "Check",r,c,F[r][c],"need_change = ", need_change
                if need_change:
                    can_change = check(F, r, c, 1, 0) or check(F, r, c, -1, 0) or check(F, r, c, 0, -1)
                    if not can_change:
                        impossible = True
                        break;
                    else:
                        n = n + 1
            elif F[r][c] == '^':
                need_change = not check(F, r, c, 0, -1)
                #print "Check",r,c,F[r][c],"need_change = ", need_change
                if need_change:
                    can_change = check(F, r, c, 1, 0) or check(F, r, c, -1, 0) or check(F, r, c, 0, 1)
                    if not can_change:
                        impossible = True
                        break;
                    else:
                        n = n + 1

            if impossible:
                break

        if impossible:
            break

    a = impossible and "IMPOSSIBLE" or str(n)

    ans = "Case #" + str(t+1) + ": " + a

    print ans
    ofile.write(ans + "\n")