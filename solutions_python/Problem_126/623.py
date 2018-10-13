import re

def get_n_value(name, n):
    sub_names = get_sub_names(name, n)
    return n_count(sub_names, n)
    
def n_count(sub_names, n):
    count = 0
    for name in sub_names:
        l = re.compile("[a e i o u]").split(name)
        if len(max(l, key=len)) >= n:
            count += 1
    return count

def get_sub_names(name, n):
    lenn = len(name)
    sub_name = []
    for i in xrange(lenn):
        for j in xrange(lenn):
            if lenn-j-i >= n:
                sub_name.append(name[i:lenn-j])
    return sub_name


file_name_in = "A-small-attempt0-1.in.txt"
file_name_out = "A-small-attempt0.out.txt"
vow = ('a', 'e', 'i', 'o',  'u')

with open(file_name_in, "r") as ff, open(file_name_out, "w") as out:
    num = int(ff.readline())
    for i in xrange(num):
        line = ff.readline().strip().split()
        name, n = line[0], int(line[1])
        n_val = get_n_value(name, n)
        print ("Case #%s: %s\n" % (i+1, n_val))
        out.write("Case #%s: %s\n" % (i+1, n_val))
    
