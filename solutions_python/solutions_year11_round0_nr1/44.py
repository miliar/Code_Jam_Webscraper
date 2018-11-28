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
    n = int(inp[0])
    seqs = map(lambda a: a.split(" ")[1:], inp[1:])
    for seq in seqs:
        s = seq[:]
        bp = 1
        op = 1
        count = 0
        while s:
            next = s[0]
            if "B" in s:
                bn = int(s[s.index("B") + 1])
            if "O" in s:
                on = int(s[s.index("O") + 1])
            if next == "B" and bn == bp:
                s = s[2:]
                if "O" in s:
                    if op < on:
                        op += 1
                    if op > on:
                        op -= 1
            elif next == "O" and on == op:
                s = s[2:]
                if "B" in s:
                    if bp < bn:
                        bp += 1
                    if bp > bn:
                        bp -= 1
            else:
                if "B" in s:
                    if bp < bn:
                        bp += 1
                    if bp > bn:
                        bp -= 1
                if "O" in s:
                    if op < on:
                        op += 1
                    if op > on:
                        op -= 1
            count += 1
        pout(str(count))

inp = get_input(sys.argv[1])    
main(inp)
write_output(sys.argv[2])
    