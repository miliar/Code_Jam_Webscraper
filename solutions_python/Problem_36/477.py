
welcome = "welcome to code jam"

def solve(case):
    i = -1
    layer = []
    while 1:
        i = case.find("w", i + 1)
        if i == -1:
            break
        layer.append(i)

    for c in welcome[1:]:
        layer2 = layer[:]
        layer = []
        for w in layer2:
            i = w
            while 1:
                i = case.find(c, i + 1)
                if i == -1:
                    break
                layer.append(i)

    return len(layer)

if __name__ == "__main__":
    case = []
    inf = open("C-small-attempt0.in", "r")
    outf = open("C-small-attempt0.out", "w")

    cc = int(inf.readline())
    for ccc in range(cc):
        case.append(inf.readline())
    
    for i, c in enumerate(case):
        num = solve(c)
        aaa = 'Case #%d: %04d' % (i + 1, num % 10000)
        print(aaa)
        print(aaa, file=outf)
    inf.close()
    outf.close()
        
