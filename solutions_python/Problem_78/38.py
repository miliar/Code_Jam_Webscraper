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
    cases = inp[1:]
    for c in cases:
        (n, pd, pg) = map(int, c.split(" "))
        for i in range(1, 101):
            if ((i * pd) % 100) == 0:
                if i <= n:
                    break
        else:
            pout("Broken")
            continue
        if pd > 0 and pg == 0:
            pout("Broken")
            continue
        if pd < 100 and pg == 100:
            pout("Broken")
            continue
        pout("Possible")

input_lines = get_input(sys.argv[1])    
main(input_lines)
write_output(sys.argv[2])
    