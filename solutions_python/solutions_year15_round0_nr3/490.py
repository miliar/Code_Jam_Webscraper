def find_index(a):
    if a == "1":
        return 0
    elif a == "i":
        return 1
    elif a == "j":
        return 2
    else:
        return 3
    
def multi(a, b):
    neg = False
    if len(a) + len(b) == 3:
        neg = True
    a_i = find_index(a[-1])
    b_i = find_index(b[-1])
    values = [["1", "i", "j", "k"],
              ["i", "-1", "k", "-j"],
              ["j", "-k", "-1", "i"],
              ["k", "j", "-i", "-1"]]
    val = values[a_i][b_i]
    if neg:
        if len(val) == 2:
            return val[-1]
        else:
            return "-" + val
    else:
        return val

def find_rest(s):
    current = s[0]
    for i in range(1, len(s)):
        current = multi(current, s[i])
    return current

def find_j(s):
    current = s[0]
    for i in range(1, len(s)):
        if current == "j":
            if find_rest(s[i:]) == "k":
                return True
        current = multi(current, s[i])
    return False

cases = int(input())
for c in range(cases):
    r = int(input().split()[1])
    string = input()
    s = string * r
    is_found = False
    if find_rest(s) == "-1":
        current = s[0]
        for i in range(1, len(s)):
            if current == "i":
                if find_rest(s[i:]) == "i":
                    is_found = find_j(s[i:])
            if is_found:
                break
            current = multi(current, s[i])
    if is_found:
        output = "YES"
    else:
        output = "NO"
    print("Case #{}: {}".format(c+1, output))