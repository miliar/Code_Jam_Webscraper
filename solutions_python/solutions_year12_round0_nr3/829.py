def is_circular(m,n):
    strm = str(m)
    strn = str(n)
    possible = [strm[i:]+strm[:i] for i in range(1,len(strm))]
    if strn in possible:
        return True
    else:
        return False

def main():
    in_dat = open('C-small-attempt0.in', 'r')
    in_lines = in_dat.readlines()[1:]
    i = 1
    for line in in_lines:
        line = line.split()
        A = int(line[0])
        B = int(line[1])
        num_circular = 0
        for m in range(A,B+1):
            for n in range(m+1,B+1):
                if is_circular(m,n):
                    num_circular += 1
        print "Case #"+str(i)+": "+str(num_circular)
        i += 1

if __name__ == "__main__":
    main()
