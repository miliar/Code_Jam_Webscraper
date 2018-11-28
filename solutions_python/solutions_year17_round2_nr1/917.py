# file = open("A-large.in", "r")
# t = int(file.readline().strip("\n"))
t = int(input().strip())
# file_out = open("output.out", "w")

risultato = ""
for m in range(t):    
    # d, n = [int(x) for x in file.readline().strip("\n").split(" ")]
    d, n = [int(x) for x in input().strip().split(" ")]
    max_tempo = 0
    for j in range(n):
        # k, s = [int(x) for x in file.readline().strip("\n").split(" ")]
        k, s = [int(x) for x in input().strip().split(" ")]
        tempo = (d - k) / s
        if j == 0 or tempo > max_tempo: max_tempo = tempo
    risultato += "Case #" + str(m + 1) + ": " + str(d/max_tempo) + ("\n" if m != t - 1 else "")
        
print(risultato)
# file_out.write(risultato)
# file_out.close()
