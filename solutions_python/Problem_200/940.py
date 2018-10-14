from sys import stdin

N = int(stdin.readline().strip())

#HIGH = chr(ord("9") + 1)

lines = []
for i in range(1, N+1):
    n = stdin.readline().strip()
    # find the end of the tidy head
    split = -1
    for j in range(len(n) - 1):
        if n[j] > n[j+1]:
            k = j
            while n[k] == n[j] and k != -1:
                k = k - 1
            split = k + 1
            break
    # if the number is not tidy
    if split != -1:
        # new number is [tidy head] + [the next digit minus 1] + [9's to end]
        s = n[:split] + chr(ord(n[split]) - 1) + "9"*(len(n)-(split + 1))
        # get rid of a heading 0.
        if s[0] == "0":
            s = s[1:]
    # if the number is tidy
    else :
        s = n
    out = "Case #%d: %s" % (i, s)
    print out
    lines.append(out)

"""
with open('googjamb.txt', 'w') as outfile:
    outfile.write("\n".join(lines))
"""
