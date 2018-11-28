import sys

fn = sys.argv[1]

f = open(fn)
tls = f.read().split('\n')

count = int(tls[0])

i = 1

case_i = 1

while i < len(tls)-1:

    bf_r = int(tls[i])
    bf_ls = set(tls[i+1:i+5][bf_r-1].split(' '))
    i += 5
    af_r = int(tls[i])
    af_ls = set(tls[i+1:i+5][af_r-1].split(' '))
    i += 5
    rs = list(bf_ls & af_ls)
    print "Case #%s: " % case_i,
    if len(rs) == 0:
        print "Volunteer cheated!"
    if len(rs) > 1:
        print "Bad magician!"
    if len(rs) == 1:
        print rs[0]

    case_i += 1
