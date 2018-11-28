# Tim Courrejou
# gcj QB

class magicka:
    def __init__(self, combos, oppos):
        self.elements = list()
        self.oppo_lookup = dict()
        self.combo_lookup = dict()
        for com in combos:
            a = com[0]
            b = com[1]
            c = com[2]
            self.combo_lookup[a+b] = c
            self.combo_lookup[b+a] = c

        for opp in oppos:
            self.oppo_lookup[opp[0]] = opp[1]
            self.oppo_lookup[opp[1]] = opp[0]

    def invoke(self, e):
        if len(self.elements) == 0:
            self.elements.append(e)
            return
        c = self.elements[len(self.elements)-1]
        if self.combo_lookup.has_key(c + e):
            self.elements[len(self.elements)-1] = self.combo_lookup[c+e]
            return
        if self.oppo_lookup.has_key(e):
            if self.oppo_lookup[e] in self.elements:
                self.elements = list()
                return
        self.elements.append(e)

    def __str__(self):
        return str(self.elements).replace("'", "")

f = open("B-small-attempt0.in", "r")
T = int(f.readline())
for i in range(0, T):

    tc = f.readline().split()

    C = int(tc[0])
    D = int(tc[C+1])
    N = int(tc[C+D+2])

    combination_list = tc[1:C+1]
    opposition_list = tc[C+2:C+D+2]
    elements = tc[C+D+3]
    print "Case #" + str(i+1) +":",
    # print "  combinations: ", combination_list
    # print "  oppositions:  ", opposition_list
    # print "  elements:     ", elements
    
    mag = magicka(combination_list, opposition_list)
    for c in elements:
        mag.invoke(c)
    print str(mag)
    
