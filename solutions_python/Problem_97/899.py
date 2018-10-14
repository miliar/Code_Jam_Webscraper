fin = "small.in"
fout = "small.out"

def chop_data(s):
    s = s.strip()
    s = s.split()
    A = int(s[0])
    B = int(s[1])
    return (A, B)

def solve(A,B):
    global _dict
    result = 0
    for i in range(A, B):
        if not _dict.has_key(i):
            done = {}
            num = str(i)
            _dict[i] = []
            for j in range(1,len(num)):
                pre_fix = num[-j:]
                sur_fix = num[:-j]
                new_num = int(pre_fix + sur_fix)
                if i < new_num:
                    if not done.has_key(new_num):
                        _dict[i].append(new_num)
                        if new_num <= B:
                            if new_num >= A:
                                done[new_num] = 1
                                result += 1
        else:
            for j in _dict[i]:
                if j <= B:
                    if j >= A:
                            result += 1
    return result

if __name__ == "__main__":
    f_in = open(fin)
    f_out = open(fout,'w')
    test_cases = int(f_in.readline())
    _dict = {}
    for t in range(0,test_cases):
        s = f_in.readline()
        A, B = chop_data(s)
        result = solve(A,B)
        s2 = "Case #" + str(t + 1) + ": " + str(result) + "\n"
        f_out.write(s2)
    f_in.close()
    f_out.close()