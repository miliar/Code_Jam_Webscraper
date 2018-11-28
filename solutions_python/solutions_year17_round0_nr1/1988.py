def pancake(S, K):
    turns = 0
    for i in range(len(S) - K + 1):
        if S[i] == "-":
            turns += 1
            S = S[:i] + turn(S[i: i + K]) + S[i + K:]
    for i in range(len(S)-K, len(S)):
        if S[i] == "-":
            return "IMPOSSIBLE"
    return turns

def turn(s):
    result = ""
    for i in s:
        if i == "+":
            result += "-"
        else:
            result += "+"
    return result


with open("E:\Python\CodeJam\A-large.in", "r") as f:
    data = f.readlines()[1:]
f.close()
with open("E:\Python\CodeJam\A-large.txt", "w") as w:
    for i in range(len(data)):
        inp = data[i].split(" ")
        w.write("Case #" + str(i + 1) + ": " + str(pancake(inp[0], int(inp[1]))) + "\n")