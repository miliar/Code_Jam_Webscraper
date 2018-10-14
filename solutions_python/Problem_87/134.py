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
    data = map(lambda a: a.strip().split(" "), inp)
    T = int(data[0][0])
    idx = 0
    for i in range(T):
        idx += 1
        X, S, R, t, N = map(int, data[idx])
        pos = 0
        total = 0
        segments = []
        for j in range(N):
            idx += 1
            B, E, w = map(int, data[idx])
            if pos < B:
                segments.append((0, B - pos))
                pos = B
            segments.append((w, E - B))
            pos = E
        if pos < X:
            segments.append((0, X - pos))
        segments.sort()
        
        for j in range(len(segments)):
            base_spd, dis = segments[j]
            section_time = 0
            if t > 0:
                spd = base_spd + R
                section_time = float(dis) / spd
                if section_time > t:
                    section_time = t
                    t = 0
                    dis -= float(spd) * section_time
                else:
                    t -= section_time
                    dis = 0
            spd = base_spd + S
            section_time += float(dis) / spd
            total += section_time
        pout(str(total))

input_lines = get_input(sys.argv[1])    
main(input_lines)
write_output(sys.argv[2])
    