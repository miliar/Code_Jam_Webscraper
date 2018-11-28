#fin = open("B-small-attempt0.in", "r")
#fout = open("B-small-attempt0.out", "w")
fin = open("B-large.in", "r")
fout = open("B-large.out", "w")

C = int(fin.readline())

def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)

def gcd_list(lists):
    ret = lists[0]
    for i in xrange(1, len(lists)):
        ret = gcd(lists[i], ret)
    return ret

for cn in xrange(1, C+1):
    item = [long(t) for t in fin.readline().strip('\n').split(' ')][1:]
    item.sort()
    need = []
    for i in xrange(1, len(item)):
        need.append(item[i] - item[i-1])
    gege = gcd_list(need)
    loli = item[0] % gege
    fout.write("Case #%d: %ld\n" % (cn, 0 if loli==0 else gege-loli))

fin.close()
fout.close()
