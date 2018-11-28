__author__ = 'banarasitippa'

import sys

def dijk_reduce ( twochars):
    dijk_lookup = {'ii': '-i', 'ij': 'k', 'ik': '-j',
                   'ji': '-k', 'jj': '-j', 'jk': 'i',
                   'ki': '-j', 'kj': '-i', 'ki': 'j'
                   }

    if twochars[0] == '1' and twochars[1] == '1':
        res = '1'
    elif twochars[0] == '1':
        res = twochars[1]
    elif twochars[1] == '1':
        res = twochars[0]
    elif twochars[0] == twochars[1]:
        res = '-1'
    else:
        res = dijk_lookup[twochars]

    return res

if len(sys.argv) < 3:
    print "usage :" + sys.argv[0] + " infile outfile"
    exit()
# open  input and output file
infile_name = sys.argv[1]
outfile_name = sys.argv[2]
infile = open(infile_name,'r')
outfile = open(outfile_name,'w')

# read number of test cases
testcases = int(infile.readline().strip())

# read test cases one by one
for test_no in range(testcases):
    line = infile.readline()
    L,X = line.split()

    line = infile.readline()
    string = line[:-1]
    chars = string * int(X)
    total_chars = int(L) * int(X)
    # pass until we filter i

    found_i = False
    found_j = False
    found_k = False
    sign = 1
    res = string[0]
    chr_pnt = 1

    while not found_i and chr_pnt < total_chars:
        if res == 'i':
            found_i = True
            res = chars[chr_pnt]
            # get next char
            if chr_pnt+1 < total_chars:
                chr_pnt += 1
        else:
            next_seq = res+chars[chr_pnt]
            res = dijk_reduce(next_seq)

            if res[0] == '-':
                res = res[1]
                sign *= -1
            chr_pnt += 1

    next_loop_not_required = False
    while found_i and not found_j and chr_pnt < total_chars:
        if res[0] == 'j':
            found_j = True
            res = chars[chr_pnt]
            # get next char
            if chr_pnt+1 < total_chars:
                chr_pnt += 1
            else:
                next_loop_not_required = True
        else:
            next_seq = res+chars[chr_pnt]
            res = dijk_reduce(next_seq)

            if res[0] == '-':
                res = res[1]
                sign *= -1

            chr_pnt += 1

    while not next_loop_not_required and found_i and found_j and chr_pnt < total_chars:
        next_seq = res+chars[chr_pnt]
        res = dijk_reduce(next_seq)

        if res[0] == '-':
            res = res[1]
            sign *= -1
        chr_pnt += 1

    if sign == 1 and found_i and found_j and res =='k':
        dataline = "Case #" + str(test_no+1) + ": YES\n"
    else:
        dataline = "Case #" + str(test_no+1) + ": NO\n"

    outfile.write(dataline)


#    dataline = "Case #" + str(test_no+1) + ": " + str(stand_req) + '\n'
#    outfile.write(dataline)

outfile.close()
infile.close()