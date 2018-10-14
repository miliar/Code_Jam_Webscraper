INPUT_FILE = "B-large.in"
OUT_FILE = "B-large.out"

class Case:
    def __init__(self, scores, surprising, value):
        self.scores = scores
        self.surprising = surprising
        self.value = value
        
    def __repr__(self):
        return "Case(%s surprising, %s value, %s scores)" % (self.surprising, self.value, self.scores)
        
    def solve(self):
        count = 0
        possible = 0
        
        for score in self.scores:
            if score % 3 == 0:
                max = score / 3
                can_inc = score > 0
            elif score % 3 == 1:
                max = score / 3 + 1
                can_inc = False
            elif score % 3 == 2:
                max = score / 3 + 1
                can_inc = True
            
            if max >= self.value:
                count += 1
            elif max + 1 == self.value and can_inc:
                possible += 1
                
        return count + min(self.surprising, possible)

def parse():
    cases = []
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        n_cases = int(lines[0])
        for i in range(n_cases):
            data = [int(x) for x in lines[i+1].split()]
            cases.append(Case(data[3:data[0]+3], data[1], data[2]))
    return cases

cases = parse()
with open(OUT_FILE, 'w') as out:
    for index, case in enumerate(cases):
        solution = case.solve()
        out.write("Case #%s: %s\n" % (index+1, solution))