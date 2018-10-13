#! /usr/bin/env python

def calc(P,K,L,tbl):
    tbl.sort()
    tbl.reverse()
    count = 0
    n = 1
    k = K
    for x in tbl:
        count += n*x
        k -= 1
        if k == 0:
            n += 1
            k = K
    return count

def main():
    ifs = open("A-large.in")
    ofs = open("out-a.txt", "w")
    num_cases = int(ifs.readline())
    for i in range(num_cases):
        P, K, L = map(int, ifs.readline().split())
        tbl = map(int, ifs.readline().split())
        ofs.write("Case #%d: %d\n" % (i + 1, calc(P,K,L,tbl)))


if __name__ == "__main__":
    main()
