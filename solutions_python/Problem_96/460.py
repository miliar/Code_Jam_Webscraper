import string

def solve(scores):
    N = scores[0]
    S = scores[1]
    p = scores[2]
    seuil = 3*p - 2
    ok = 0
    for score in scores[3:]:
        if score < p:
            continue
        elif score >= seuil:
            ok += 1
        elif score >= seuil - 2 and S > 0:
            ok += 1
            S -= 1
    return ok

def main():
    inp = open('B-large.in', 'r')
    out = open('B-large.out', 'w')
    num_case = int(inp.readline())
    i = 1
    for line in inp:
        instance = map(int, line.split())
        out.write("Case #"+str(i)+": "+str(solve(instance))+'\n')
        i+=1
    inp.close()
    out.close()

if __name__ == "__main__":
    main()
