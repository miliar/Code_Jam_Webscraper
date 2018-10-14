def solve(S):
    N = 0
    ans = 0
    for i, s in enumerate(S):
        if N < i:
            ans += i - N
            N = i
        N += s
    return ans



if __name__ == "__main__":
    with open("input1.txt") as fin, open("output1.txt", "w") as fout:
        N = fin.readline()
        answers = []
        for line in fin:
            M, S = line.split()
            S = map(int, S)
            answers.append(solve(S))

        res = ""
        for i, ans in enumerate(answers):
            res += "Case #%d: %s\n" % (i+1, ans)
        fout.write(res)
