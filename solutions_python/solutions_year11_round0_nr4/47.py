import math
import sys

outf = []
def pout(text):
    outf.append("Case #" + str(pout.case) + ": " + text + "\n")
    pout.case += 1
pout.case = 1

def get_input(infname):
    with open(infname, "r") as f:
        return map(lambda a: a.strip(), f.readlines())

def write_output(outfname):
    with open(outfname, "w") as f:
        for line in outf:
            f.write(line)

# DEPTH_MAX = 100
# prob_dic = {}
# ev_dic = {}
# ev_dic[0] = 0.0
# ev_dic[1] = 0.0

# def get_prob(k, n):
    # if k == 0:
        # return 1.0 / math.factorial(n)
    # if k == 1:
        # return 0.0
    # if (k, n) in prob_dic:
        # return prob_dic[(k, n)]
    # coef = 1.0 / math.factorial(n-k)
    # prob_sum = 0.0
    # for i in range(k):
        # prob_sum += get_prob(i, k)
    # result = coef * (1 - prob_sum)
    # prob_dic[(k, n)] = result
    # return result
    
# def get_ev(n):
    # return get_ev_2(n, DEPTH_MAX)
    
# def get_ev_2(n, d):
    # if d <= 0:
        # return 0.0
    # if n in ev_dic:
        # return ev_dic[n]
    # ev = 1.0
    # for i in range(2, n+1):
        # ev += get_prob(i, n) * get_ev_2(i, d-1)
    # ev_dic[n] = ev
    # return ev
    
def main(inp):    
    lines = map(lambda a: a.split(" "), inp[1:])
    seqs = []
    for i in range(len(lines)):
        if i % 2:
            seqs.append(map(lambda a: int(a)-1, lines[i]))
    for seq in seqs:
        s = seq[:]
        cov = map(lambda a: False, s)
        #gns = []
        ev = 0.0
        gidx = -1
        for i in range(len(s)):
            if cov[i]:
                continue
            if s[i] == i:
                cov[i] = True
                continue
            if gidx == -1:
                cov[i] = True
                idx = s[i]
                gn = 1
                while not cov[idx]:
                    cov[idx] = True
                    idx = s[idx]
                    gn += 1
                #gns.append(gn)
                ev += gn
        #ev = 0.0
        #for n in gns:
        #    ev += get_ev(n)
        pout(str(ev))
            
inp = get_input(sys.argv[1])    
main(inp)
write_output(sys.argv[2])

    