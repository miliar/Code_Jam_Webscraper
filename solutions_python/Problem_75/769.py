class MagickaSpell:
    
    base_elements = set(["Q","W","E","R","A","S","D","F"])

    def __init__(self, spell, combines, opposes):
        self.element_list = []
        self.spell = spell
        self.combines = combines
        self.opposes = opposes
        

    def _combine(self):
        last_two = "".join(self.element_list[-2:])
        if last_two in self.combines:
            self.element_list.pop()
            self.element_list.pop()
            self.element_list.append(self.combines[last_two])
        return

    def _oppose(self):
        for op in self.opposes:
            if op <= set(self.element_list):
                self.element_list = []
                break
        return


    def evaluate(self):
        for letter in spell:
            self.element_list.append(letter)
            if len(self.element_list) >= 2:
                self._combine()
                self._oppose()
        return self.element_list


if __name__ == "__main__":

    out_fmt = "Case #{}: [{}]\n"

    with open("B-large.in", "r") as fin, open("B-large.out", "w") as  fout:
        ncases = int(fin.readline())
        for case in range(1, ncases + 1):
            
            raw_case = fin.readline().split(" ")

            combines = {}
            ncombines = int(raw_case.pop(0))
            for nc in range(ncombines):
                rcp = raw_case.pop(0)
                reactants = rcp[:2]
                products = rcp[-1]
                combines[reactants] = products
                combines[reactants[::-1]] = products

            opposes = []
            nopposes = int(raw_case.pop(0))
            for no in range(nopposes):
                opposes.append(frozenset(raw_case.pop(0)))
            
            nchar = int(raw_case.pop(0))
            spell = raw_case.pop(0).strip()
                
            ms = MagickaSpell(spell = spell,
                              combines = combines,
                              opposes  = opposes)

            fout.write(out_fmt.format(case, ", ".join(ms.evaluate())))

            
        
