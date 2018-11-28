from collections import defaultdict
import sys
       
def go(filename):
    with open(filename) as f:
        with open("out.txt", "w") as output:
            for case in range(1, int(f.readline()) + 1):
                combos = defaultdict(dict)
                opps = defaultdict(set)
                tokens = f.readline().split()
                num_combos = int(tokens[0])
                for token in tokens[1:(num_combos + 1)]:
                    a, b, c = token[0], token[1], token[2]
                    combos[a][b] = combos[b][a] = c
                num_opps = int(tokens[1 + num_combos])
                for token in tokens[2 + num_combos:(2 + num_combos + num_opps)]:
                    a, b = token[0], token[1]
                    opps[a].add(b)
                    opps[b].add(a)
                result = []
                for e in tokens[-1]:
                    if result and e in combos[result[-1]]:
                        result[-1] = combos[result[-1]][e]
                    elif any([e in opps[v] for v in result]):
                        result = []
                    else:
                        result.append(e)                 
                output.write("Case #%d: [%s]\n" % (case, ", ".join(result)))            

def main():
    if len(sys.argv) < 1:
        print "Usage: %s <filename>" % os.path.basename(sys.argv[0])
    else:
        go(sys.argv[1])

if __name__ == "__main__":
    main()
