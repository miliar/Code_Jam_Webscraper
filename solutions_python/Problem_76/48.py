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
    lines = map(lambda a: a.split(" "), inp[1:])
    bags = []
    for i in range(len(lines)):
        if i % 2:
            bags.append(map(int, lines[i]))
    for bag in bags:
        if reduce(lambda a, b: a^b, bag) or (len(bag) < 2):
            pout("NO")
        else:
            pout(str(sum(bag)-min(bag)))

inp = get_input(sys.argv[1])    
main(inp)
write_output(sys.argv[2])
    