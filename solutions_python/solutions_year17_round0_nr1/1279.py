def minFlips(S, K):
    flips = 0
    for i in range(len(S)):
        if(S[i] == "-"):
            if(i > len(S) - K):
                return "IMPOSSIBLE"
            s = S[:i]
            for j in range(i, i+K):
                if(S[j] == "+"):
                    s += "-"
                else:
                    s += "+"
            s += S[i+K:]
            S = s
            flips += 1
    return str(flips)

def main():
    infile = open("A-large.in", "r")
    outfile = open("A-large.out", "w")
    T = int(infile.readline())
    for i in range(T):
        line = infile.readline()
        line = line.split(" ")
        S = line[0]
        K = int(line[1])
        outfile.write("Case #"+str(i+1)+": "+minFlips(S,K)+"\n")

    infile.close()
    outfile.close()
