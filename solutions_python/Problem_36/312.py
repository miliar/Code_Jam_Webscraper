def subsequences(target, string):
    if target == "":
        return 1
    out = 0
    for x in range(len(string)):
        if string[x] == target[0]:
            out += subsequences(target[1:], string[x+1:])
    return out

f = open('C-small-attempt0.in.txt', 'r')
N = int(f.readline().strip())
output = open('welcome_to_code_jam_output.txt', 'w')
for x in range(N):
    output.write("Case #" + str(x+1) + ": " + str(subsequences('welcome to code jam', f.readline().strip())).zfill(4)[-4:] + "\n")
f.close()
output.close()
