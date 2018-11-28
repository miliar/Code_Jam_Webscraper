def last_word(s):
    if s == "":
        return ""
    elif len(s) == 1:
        return s
    elif len(s) == 2:
        if s[0] < s[1]:
            return s[::-1]
        else:
            return s
    ret = s[0]
    temp = s[0]
    for i in range(1,len(s)):
        if s[i] >= temp:
            temp = s[i]
            ret = temp + ret
        else:
            ret += s[i]
    return ret

with open("input.txt") as f:
    output= open("output.txt","w")
    num = int(f.readline())
    for i in range(num):
        line = f.readline().strip()
        output.write("Case #{}: {}\n".format(i+1,last_word(line)))
    output.close()

        
