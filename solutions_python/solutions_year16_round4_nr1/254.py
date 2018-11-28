from itertools import permutations
def reader(in_file):
    return in_file.getInts()


def check(s):
    while len(s) != 1:
        news = ""
        for i in range(0,len(s),2):
            if s[i] == s[i+1]:
                return False
            elif s[i] == "R" and s[i+1] == "P":
                news += "P"
            elif s[i] == "P" and s[i + 1] == "R":
                news += "P"

            elif s[i] == "R" and s[i + 1] == "S":
                news += "R"
            elif s[i] == "S" and s[i + 1] == "R":
                news += "R"

            elif s[i] == "P" and s[i + 1] == "S":
                news += "S"
            elif s[i] == "S" and s[i + 1] == "P":
                news += "S"
        s = news
    return True


def solver((n, r, p, s)):
    string = "R"*r + "P" * p + "S" * s
    assert len(string) == 2**n
    hmm = filter(check, permutations(string, len(string)))
    if len(hmm) == 0:
        return "IMPOSSIBLE"
    hmm.sort()

    return "".join(hmm[0])

if __name__ == "__main__":
    # GCJ library publically available at http://ideone.com/2PcmZT
    from GCJ import GCJ
    GCJ(reader, solver, "a", "A").run()
