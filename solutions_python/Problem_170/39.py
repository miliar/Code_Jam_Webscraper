__author__ = 'PrimuS'

import multiprocessing as mp


def fun(a):
    if __name__ == '__main__':
        mp.freeze_support()
    k, num, ss = a
    up = 1 << (num - 2)
    res = 200000
    eset1 = set()
    eset2 = set()
    for w in ss[0]:
        eset1.add(w)
    for w in ss[1]:
        eset2.add(w)

    for m in range(up):
        set1 = set()
        set2 = set()


        for i in range(num-2):
            flag = m & (1 << i)
            for w in ss[2 + i]:
                if flag:
                    set1.add(w)
                else:
                    set2.add(w)

        set1.update(eset1)
        set2.update(eset2)
        set1.intersection_update(set2)

        ctr = len(set1)
        # if len(set1) > len(set2):
        #     for w in set1:
        #         if w in set2:
        #             ctr += 1
        # else:
        #     for w in set2:
        #         if w in set1:
        #             ctr += 1

        res = min(res, ctr)
    print(k, "finished")
    return (k, res)

def main():
    f = open("d:\\dev\\acm\\codeJam 2015\\C-small-attempt1.in", "r")
    of = open("d:\\dev\\acm\\codeJam 2015\\C-small-res_last.txt", "w")
    #f = open("d:\\dev\\acm\\codeJam 2015\\in.txt", "r")
    #of = open("d:\\dev\\acm\\codeJam 2015\\res.txt", "w")

    T = int(f.readline())
    nn = [0] * T
    sss = [0] * T
    for t in range(1, T + 1):
        nn[t-1] = int(f.readline())
        sss[t-1] = [""] * nn[t-1]
        for i in range(nn[t-1]):
            sss[t-1][i] = list(f.readline().strip().split())


        #print("Case #{:d}: {:d}".format(t, res), file=of)
        #print(t)
    pool = mp.Pool(processes=8)
    results = pool.map(fun, zip(range(T), nn, sss))
    results.sort()
    for r in results:
        print("Case #{:d}: {:d}".format(r[0] + 1, r[1]), file=of)
    print(results)


    of.close()

if __name__ == '__main__':
    mp.freeze_support()
    main()