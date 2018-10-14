
def main():
    """A"""

    name = "A-large"

    fin = open(name + ".in", "r")
    fout = open(name + ".out", "w")

    T = int(fin.readline())
    
    for i in range(0, T):
        S, K = fin.readline().split(' ')
        K = int(K)
        S = list(S)
        
        steps = 0
        impossible = False
        for j in range(0, len(S)):
            if S[j] == '+':
                continue
            else:
                if (j + K) > len(S):
                    impossible = True
                    break

                for k in range(0, K):
                    if S[j + k] == '+':
                        S[j + k] = '-'
                    else:
                        S[j + k] = '+'             
                steps += 1

        if impossible:
            fout.write("Case #{0}: IMPOSSIBLE\n".format(i + 1))
        else:
            fout.write("Case #{0}: {1}\n".format(i + 1, steps))
            
        impossible = False
                
main()