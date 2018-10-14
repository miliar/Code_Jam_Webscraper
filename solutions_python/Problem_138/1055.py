out = open("DLargeOut.txt", 'w')
text = open("DLarge.txt", 'r')
text = text.readlines()

def solve(a, c):
    score = 0
    b = [i for i in c]
    for i in a:
        m = float("inf")
        for j in b[::-1]:
            if j < i:
                break
            if j < m and j > i:
                m = j
        if m == float("inf"):
            b.remove(b[0])
            score += 1
        else:
            b.remove(m)
    return score

    

tc = int(text[0])
line = 0
for c in range(tc):
    line += 1
    b = int(text[line])
    line += 1
    N = [float(num) for num in text[line].split()]
    N.sort()
    line += 1
    K = [float(num) for num in text[line].split()]
    K.sort()
    ans1 = solve(N, K)
    ans2 = len(K) - solve(K, N)
    ans = str(ans2) + " " + str(ans1)
    #print("Case #" + str(c + 1) + ": " + str(ans) + "\n")
    out.write("Case #" + str(c + 1) + ": " + str(ans) + "\n")
out.close()
