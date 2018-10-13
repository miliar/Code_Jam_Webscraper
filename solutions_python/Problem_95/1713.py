alpha = "abcdefghijklmnopqrstuvwxyz"
key =   "yhesocvxduiglbkrztnwjpfmaq"

fin = open("a.in")
fout = open("a.out", "w")

N = int(fin.readline())

for i in range(N):
    sentence = fin.readline().strip()
    answer = ""
    length = len(sentence)

    for k in range(length):
        if (sentence[k] in alpha):
            pos = alpha.find(sentence[k])
            answer += key[pos]
        else:
            answer += sentence[k]

    fout.write("Case #" + str(i + 1) + ": " + answer + "\n")

fout.close()
fin.close()
