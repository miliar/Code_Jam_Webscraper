def rev(sim):
    if sim == "+":
        return "-"
    return "+"

def calc(file):
    s, k = file.readline().split()
    k = int(k)
    s = list(s)
    ans = 0
    for i in xrange(len(s)-k+1):
        if s[i] == '+':
            continue
        ans += 1
        for j in range(k):
            s[i+j] = rev(s[i+j])
    for i in s:
        if i == "-":
            ans = "IMPOSSIBLE"
            break
    return ans

def main():
    file = open("input.txt")
    fl_o = open("output.txt", 'w')
    T = int(file.readline())
    for t in range(T):
        ans = calc(file)
        fl_o.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
    fl_o.close()

main()