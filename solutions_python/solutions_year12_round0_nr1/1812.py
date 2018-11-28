INPUT_FILE = "A-small-attempt0.in"
OUT_FILE = INPUT_FILE + ".out"

INPUT_DATA = "z y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
OUTPUT_DATA = "q a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

def parse():
    cases = []
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        n_cases = int(lines[0])
        for i in range(1, n_cases+1):
            cases.append(lines[i].strip('\n'))
    return cases

def write_solutions(solutions):
    with open(OUT_FILE, 'w') as out:
        for index, solution in enumerate(solutions):
            out.write("Case #%s: %s\n" % (index+1, solution))

def build_mapping():
    return dict(zip(INPUT_DATA, OUTPUT_DATA))

def solve(map, str):
    return ''.join([map[c] for c in str])
        
map = build_mapping()
cases = parse()
solutions = [solve(map, case) for case in cases]

write_solutions(solutions)
