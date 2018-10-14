
def calc(file):
    n = list(str(int(file.readline())))
    n.insert(0, '0')
    ind = -1
    for i in xrange(1, len(n), 1):
        if n[i] < n[i-1]:
            ind = i
            break
    if ind == -1:
        return int("".join(n))
    while n[ind-1] == n[ind-2]:
        ind -= 1
    n[ind-1] = str(int(n[ind-1]) - 1)
    for i in xrange(ind, len(n), 1):
        n[i] = "9"
    return int("".join(n))

def main():
    file = open("input.txt")
    fl_o = open("output.txt", 'w')
    T = int(file.readline())
    for t in range(T):
        ans = calc(file)
        fl_o.write("Case #" + str(t+1) + ": " + str(ans) + "\n")
    fl_o.close()

main()