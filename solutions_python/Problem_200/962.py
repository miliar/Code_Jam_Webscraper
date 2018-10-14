import fileinput
import pdb
import sys

def brute_force_tidy(N):
    while N > 0:
        if str(N) == "".join(sorted(str(N))):
            return N
        N -= 1

def smarter_tidy(N):
    s_N = str(N)

    new_s = ""
    for i, c in enumerate(s_N[:-1]):
        if int(c) <= int(s_N[i+1]):
            new_s += c
        else:
            new_c = str(int(c) - 1)
            num_c = s_N[:i+1].count(c)
            new_s = new_s[:i - num_c + 1] + new_c
            new_s += "9" * (len(s_N) - len(new_s))
            break
    if len(s_N) == len(new_s) + 1: new_s += s_N[-1]
    if new_s[0] == "0":
        new_s = new_s[1:]
        new_s = new_s.replace("0", "9")
    return new_s

def ccheck(N):
    if(smarter_tidy(N) != str(brute_force_tidy(N))):
        print("DIFF:{} OLD: {} NEW: {}".format(N, brute_force_tidy(N), smarter_tidy(N)), file=sys.stderr)

if __name__ == "__main__":
    for case, line in enumerate(fileinput.input()):
        if case == 0:
            continue
        N = int(line.strip())
        print("Case #{}: {}".format(case, smarter_tidy(N)))
