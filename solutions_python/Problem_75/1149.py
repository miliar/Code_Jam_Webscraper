


if __name__ == '__main__':
    def do_combs():
        if len(gen) < 2: return
        for comb in combs:
            if (comb[0] == gen[-1] and comb[1] == gen[-2]) or (comb[0] == gen[-2] and comb[1] == gen[-1]):
                gen.pop()
                gen.pop()
                gen.append(comb[2])
    
    def do_opps():
        opp_char = gen[-1]
        for opp in opps:
            if opp_char in opp:
                if opp[1-opp.index(opp_char)] in gen: return []
        return gen

    inn = open("problems/B-small-attempt1.in", "r")
    out = open("solutions/amit1", "w")
    l = inn.readline()
    for i in range(0, int(l)):
        combs = []
        opps = []
        p = ''
        t = inn.readline().split(' ')
        comb_num = int(t[0])
        for j in range(0, comb_num):
            combs.append(t[j+1])
        opp_num = int(t[comb_num+1])
        for j in range(0, opp_num):
            opps.append(t[j+comb_num+2])
        p = t[comb_num+opp_num+3]
        
        gen = []
        for c in p:
            if c == '\n': break
            gen.append(c)
            do_combs()
            gen = do_opps()
            
        out.write('Case #' + str(i+1) + ': [' + ", ".join(gen) + "]\n")
            
    inn.close()
    out.close()