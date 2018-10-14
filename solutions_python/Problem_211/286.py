file = open("C-small-1-attempt0.in", "r")
# t = int(file.readline().strip("\n"))
t = int(input().strip())
file_out = open("output.out", "w")

risultato = ""
for m in range(t):
    # n, k = [int(x) for x in file.readline().strip("\n").split(" ")]
    n, k = [int(x) for x in input().strip().split(" ")]
    # u = float(file.readline().strip("\n"))
    u = float(input().strip())
    # p = sorted([float(x) for x in file.readline().strip("\n").split(" ")])
    p = sorted([float(x) for x in input().strip().split(" ")])
    fine = False
    i = 1
    while not fine:
        prob_media = (sum(p[:i]) + u) / i
        if i == len(p) or prob_media <= p[i]: fine = True
        else: i += 1
    prob = prob_media ** i
    for j in range(i, len(p)): prob *= p[j]    
    risultato += "Case #" + str(m + 1) + ": " + str(prob) + ("\n" if m != t - 1 else "")
    
print(risultato)
# file_out.write(risultato)
# file_out.close()
