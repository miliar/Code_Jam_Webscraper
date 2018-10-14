inp = open("in.txt", "r")
out = open("out.txt","w")
T= int((inp.readline()).rstrip())
for i in range(T):
    args=list(map(int,list(((inp.readline()).rstrip()).split())))
    n = args[0]
    k = args[1]
    ls = [n]
    mrg_sets = {n: 1}
    while True:
        m = max(ls)
        tot = mrg_sets[m]
        mrg_sets.pop(m)
        if k <= tot:
            m -= 1
            break
        k -= tot
        ls.remove(m)
        m -= 1
        hp = m - m // 2
        hd = m // 2
        if hp == hd:
            if hp in mrg_sets:
                mrg_sets[hp] += tot * 2
            else:
                mrg_sets[hp] = tot * 2
            if hp not in ls:
                ls.append(hp)
        else:
            if hp in mrg_sets:
                mrg_sets[hp] += tot
            else:
                mrg_sets[hp] = tot
            if hd in mrg_sets:
                mrg_sets[hd] += tot
            else:
                mrg_sets[hd] = tot
            if hp not in ls:
                ls.append(hp)
            if hd not in ls:
                ls.append(hd)
    out.write("Case #" + str(i+1) + ": " + str(int(m - m//2)) + ' ' + str(int(m//2)) + "\n")
