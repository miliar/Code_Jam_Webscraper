import re

def rl(f):
    return f.readline().strip()

def main():
    inp = open("B-small-attempt2.in")
    out = open("B-small.out", "w")
    
    T = int(rl(inp))
    for c in range(1, T+1):
        N, M = map(int, rl(inp).split(" "))
        words = []
        for n in range(N):
            words.append(rl(inp))
            
        print >>out, "Case #%d:" % c,
        for m in range(M):
            l = rl(inp)
            b = -1
            bw = None
            for word in words:
                points = 0
                letters = ""
                nwords = [w for w in words if len(w) == len(word)]
                if len(nwords) == 1:
                    if points > b:
                        b = points
                        bw = word
                        continue
                    
                all_letters = set("".join(nwords))
                for letter in l:
                    if letter in all_letters:
                        if letter in word:
                            letters += letter
                            p = re.compile("[^" + letters + "]")
                            blanked = p.sub(".", word)
                            nwords = [w for w in nwords if p.sub(".", w) == blanked]
                            all_letters = set("".join(nwords))
                            if len(nwords) == 1:
                                if points > b:
                                    b = points
                                    bw = word
                                    break
                        else:
                            nwords = [w for w in nwords if letter not in w]
                            all_letters = set("".join(nwords))
                            points += 1
            if m == M-1:
                print >>out, bw
            else:
                print >>out, bw,           
    inp.close()
    out.close()

if __name__ == '__main__':
    main()