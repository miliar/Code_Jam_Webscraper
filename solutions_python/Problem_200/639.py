def main(file_in, file_out):
    lines = file_in.readlines()[1::]
    writeSolution(file_out, [solve(line.strip()) for line in lines])

def solve(line):
    num = [int(ch) for ch in line]
    idx = 0
    pNum = num[idx]
    res = False
    for i in range(len(num)):
        if num[i] < pNum:
            res = True
            break
        if num[i] > pNum:
            idx = i
            pNum = num[i]
    if res:
        t = num[0:idx] + [num[idx] - 1] + [9 for _ in range(len(num) - idx - 1)]
        s = ''.join([str(n) for n in t])
        if s[0] == '0': return s[1:]
        else: return s
    else:
        return line
        
def writeSolution(file, slns):
    lines = ["Case #{}: {}".format(n+1, slns[n]) for n in range(len(slns))]
    file_out.write('\n'.join(lines))

def getInt(line):
    return int(line.strip())

def getInts(line):
    return [int(token.strip()) for token in line.split()]

if __name__ == "__main__":
    with open("test.in", "r") as file_in, open("test.out", "w") as file_out:
            main(file_in, file_out)
            file_out.close()