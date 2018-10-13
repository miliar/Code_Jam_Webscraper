dic = {"y":"a", "e":"o", "q":"z", "j":"u", "p":"r", "m":"l", "s":"n", "l":"g", "c":"e", "k":"i",
"d":"s", "x":"m", "v":"p", "n":"b", "r":"t", "i":"d", "b":"h", "t":"w", "a":"y", "h":"x", "w":"f", "f":"c",
"o":"k", "u":"j", "z":"q", "g":"v"," ":" "}
def solve(line):
    out = ""
    for i in range(0,len(line)):
        out += dic[line[i]]
    return out
input = open("A-small-attempt0.in","rU")
out = open("out_speak.out","w")
T = int(input.readline().rstrip('\n'))
for i in range(0, T):
    line = input.readline().rstrip('\n')
    out.write("Case #" + str(i + 1) + ": " + solve(line) + "\n")
out.close()