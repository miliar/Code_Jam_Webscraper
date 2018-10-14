def permutations(string):
    if len(string) == 1:
        return [string]
    out = []
    for x in range(len(string)):
        perms = permutations(string[:x]+string[x+1:])
        for p in perms:
            out.append(string[x] + p)
    return out

input_file = open("B-small-attempt2.in.txt", "r").readlines()
output_file = open("output.txt", "w")
T = int(input_file.pop(0).strip())
for case in range(T):
    output_file.write("Case #" + str(case+1) + ": ")
    N = int(input_file.pop(0).strip())
    string = ""
    for x in str(N):
        if x != "0":
            string += x
    p = permutations(string)
    p.sort()
    while int(p[-1]) <= N:
        string += "0"
        p = permutations(string)
        p.sort()
    for x in p:
        if int(x) > N:
            output_file.write(str(x) + "\n")
            break
output_file.close()
    
