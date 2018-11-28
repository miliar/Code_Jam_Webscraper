__author__ = 'narun'
import itertools

def write_output(fh, case, output_list):
    fh.write('Case #'+str(case)+': '+' '.join(output_list)+'\n')


filename = 'D-large.in'
outfile = 'D-large.out'
# filename = 'A-large-practice.in'
# outfile = 'A-large-practice.out'
input_file = open(filename, 'r')
output_file = open(outfile, 'w')
debug = False

num = int(input_file.readline())
for i in range(num):
    nblock = int(input_file.readline())
    naomi = input_file.readline()
    ken = input_file.readline()
    ns = [(float(x), 'n') for x in naomi.split()]
    # ns.sort()
    print(ns, len(ns)) if debug else None
    ks = [(float(x), 'k') for x in ken.split()]
    # ks.sort()
    print(ks, len(ks)) if debug else None
    both = list(itertools.chain(ns, ks))
    both.sort()
    print(both, len(both)) if debug else None
    point = nblock
    k = 0
    war = 0
    war_n = 0
    war_k = 0
    for index in range(2*nblock):
        if k == 0:
            if both[index][1] == 'n':
                point -= 1
            else:
                k += 1
        else:
            if both[index][1] == 'n':
                k -= 1
            else:
                k += 1
        if both[index][1] == 'n':
            war_n += 1
        else:
            if war_n > 0:
                war_n -= 1
            else:
                war += 1

        # print(point) if debug else None
        # print(k) if debug else None
        # print(war) if debug else None
    print(point) if debug else None
    # exit()
    # c = float(arr[0])
    # f = float(arr[1])
    # x = float(arr[2])
    # nc = 0
    # t = 0
    # print(c, f, x) if debug else None
    # # while nc*c/2 + x/(2+nc*f) > (nc+1)*c/2 + x/(2+(nc+1)*f):
    # while x/(2+nc*f) > c/(2+nc*f) + x/(2+(nc+1)*f):
    #     t += c/(2+nc*f)
    #     nc += 1
    #     print(t) if debug else None
    # t += x/(2+nc*f)
    # print(t) if debug else None
    write_output(output_file, i+1, [str(point), str(war)])