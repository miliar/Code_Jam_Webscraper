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
          
def main(inp):    
    idx = 1
    for i in range(int(inp[0])):
        bins = map(lambda a: [], range(10))
        answers = []
        (n, m) = map(int, inp[idx].split(" "))
        words = inp[(idx+1):(idx+1+n)]
        orders = inp[(idx+1+n):(idx+1+n+m)]
        idx += n + m + 1
        for o in orders:
            parts = map(lambda a: map(lambda b: "_", a), words)
            points = map(lambda a: 0, words)
            for c in o:
                old_parts = []
                for i in range(n):
                    old_parts.append(parts[i][:])
                    for j in range(len(words[i])):
                        if words[i][j] == c:
                            parts[i][j] = c
                for i in range(n):
                    if parts[i] == old_parts[i]:
                        for j in range(n):
                            if (old_parts[i] == old_parts[j]) and (parts[i] != parts[j]):
                                points[i] += 1
                                break
            max_points = 0
            max_idx = 0
            for i in range(n):
                if points[i] > max_points:
                    max_points = points[i]
                    max_idx = i
            answers.append(words[max_idx])
        pout(" ".join(answers))
                        
                    
                    
                
        
        
        

input_lines = get_input(sys.argv[1])    
main(input_lines)
write_output(sys.argv[2])
    