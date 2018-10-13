#! /usr/bin/python



def read_input():
    fin = open("B-small-attempt0.in", "r")
    ret = []
    for index, line in enumerate(fin):
        if index is 0:
            continue
        ln = line.strip().split()
        redux_N = int(ln[0])
        index = 1
        redux = {}
        for i in xrange(redux_N):
            rule = ln[index]
            redux[rule[:2]] = rule[-1]
            redux[rule[:2][::-1]] = rule[-1]
            index += 1
        print "redux =", redux
        elim_N = int(ln[index])
        index += 1
        elim = {}
        for i in xrange(elim_N):
            rule = ln[index]
            elim[rule[0]] = rule[1]
            elim[rule[1]] = rule[0]
            index += 1
        print "elim =",elim
        m = ln[index + 1]
        print "m =", m
        ret.append((redux, elim, m))
    return ret

def write_output(ret):
    fout = open("b.out", "w")
    for index, r in enumerate(ret):
        fout.write("Case #%d: %s\n" % (index +1, str(r).replace('\'', '')))
    fout.close()

def main():
    print "problema B"
    l = read_input()
    ret = []
    for (redux, elim, m) in l:
        stack = []
        for c in m:
            stack.append(c)
            last2 = stack[len(stack)-2:len(stack)]
            if len(last2) == 2:
                repl = redux.get(''.join(last2))
                if repl:
                    print "replacing " +str(last2) +" with "+repl
                    stack = stack[0:len(stack)-2]
                    stack.append(repl)
                    last2 = [repl]
                for e in last2:
                    for old in stack:
                        if elim.get(e) == old:
                            stack = []
                            break
                    if len(stack) == 0:
                        break
        ret.append(stack)
    write_output(ret)



if __name__ == "__main__":
    main()
