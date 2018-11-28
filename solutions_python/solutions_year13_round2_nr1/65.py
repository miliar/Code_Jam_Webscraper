import sys

def main(fin, fout):
    T = int(fin.readline())
    for t in range(1,T+1):
        A = int(fin.readline().split()[0])
        modes = sorted(int(x) for x in fin.readline().split())


        print("Case #{:d}: {:d}".format(t, walkthrough(A, modes)))


def walkthrough(cur_size, modes):
    if len(modes) == 0:
        return 0
    if cur_size > modes[0]:
        return walkthrough(cur_size + modes[0], modes[1:])

    num_ops_needed = 0
    new_size = cur_size
    while new_size <= modes[0] and num_ops_needed < len(modes):
        new_size += new_size - 1
        num_ops_needed += 1

    if num_ops_needed == len(modes):
        return num_ops_needed

    return num_ops_needed + walkthrough(new_size + modes[0], modes[1:])


if __name__=="__main__":
    if len(sys.argv) > 1:
        fin = open(sys.argv[1])
    else:
        fin = sys.stdin

    if len(sys.argv) > 2:
        fout = open(sys.argv[2], 'w')
    else:
        fout = sys.stdout

    main(fin,fout)
