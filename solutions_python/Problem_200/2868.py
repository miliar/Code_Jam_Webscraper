
def solve(last_number):
    ret = ""
    last_str = str(last_number)
    last_list = list(map(int, list(last_str)))
    for i in range(len(last_list)):
        target = int(last_str[i:])
        limit = int(str(last_list[i]) * (len(last_list) - i))
        if target >= limit:
            ret += last_str[i]
        else:
            if last_list[i] > 1:
                ret += str(last_list[i] - 1)
            ret += "9" * (len(last_list) - i - 1)
            break
    return ret


fin = open("B-large.in", "r")
fout = open("out.txt", "w")

T = int(fin.readline())

for t in range(T):
    last_number = int(fin.readline())

    ans = solve(last_number)
    fout.write("Case #%d: %s\n"%(t+1, ans))

fin.close()
fout.close()