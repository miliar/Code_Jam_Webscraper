## Setup
# Task letter
TASK="B"

## Input templates
# Line as int
#int(infile.readline())
# Line as many ints
#(int(s) for s in infile.readline().split())

## Precalculation
#print("Precalculation...")
#print("Precalculation done.")

## Calculation
print("Calculation...")
with open(TASK+".in") as infile:
    with open(TASK+".out",mode="wt") as outfile:
        cases = int(infile.readline())
        for ncase in range(cases):
            # Perform all nessesary calculation
            case = infile.readline().split()
            print(case)
            lcombs = [case[i+1] for i in range(int(case[0]))]
            combs = dict()
            for c in lcombs:
                combs[c[0] + c[1]] = c[2]
                combs[c[1] + c[0]] = c[2]
            del case[0:int(case[0])+1]
            print(combs)
            lopps = [case[i+1] for i in range(int(case[0]))]
            opps = dict()
            for o in lopps:
                if o[0] not in opps: opps[o[0]] = set()
                opps[o[0]].add(o[1])
                if o[1] not in opps: opps[o[1]] = set()
                opps[o[1]].add(o[0])
            del case[0:int(case[0])+1]
            print(opps)
            seq = case[1]
            cur = []
            for c in seq:
                cur.append(c)
                while ''.join(cur[-2:]) in combs:
                    cur[-2:] = combs[''.join(cur[-2:])]
                if cur[-1] not in opps: continue
                for c in opps[cur[-1]]:
                    if c in cur:
                        cur = []
            outfile.write("Case #{nc}: {data}\n".format(nc=ncase+1,data='[{c}]'.format(c=', '.join(cur))))
print("Calculation done.")
