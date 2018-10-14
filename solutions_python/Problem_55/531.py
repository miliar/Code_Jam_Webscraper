# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="nsho"
__date__ ="$2010/05/08 8:00:25$"

debug=True
def inc_index(index, cap):
    index += 1
    if index >= cap:
        index = 0
    return index

def coaster(nr_time, capacity, group_list):
    if sum(group_list) <= capacity:
        total = nr_time * sum(group_list)
    else:
        gp = curr_gp = 0
        total = 0
        for i in range(0, nr_time):
            curr_total = 0
            while 1:
                if (curr_total + group_list[curr_gp] > capacity):
                    break
                curr_total += group_list[curr_gp]
                curr_gp = inc_index(curr_gp, len(group_list))
                if curr_gp == gp or curr_total == capacity:
                    break
            gp = curr_gp
            total += curr_total
            if debug:
                print curr_total
    return total

if __name__ == "__main__":
    print "Hello World"
    fname = "in.txt"
    outf = fname + ".out"
    with open(fname, 'r') as fp:
        line = fp.readline()
        nr_case = int(line)
        case = 1
        with open(outf, 'w') as out_fp:
            for i in range(0, nr_case):
                R, k, N = fp.readline().split()
                g = list()
                line = fp.readline()
                for nr_g in line.split():
                    g.append(int(nr_g))
                total = coaster(int(R), int(k), g)
                outline = "Case #%d: %d\n" % (case, total)
                out_fp.write(outline)
                print outline,
                case += 1




