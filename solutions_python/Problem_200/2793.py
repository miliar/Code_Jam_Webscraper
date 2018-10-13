
filename = r"F:\Nir\Downloads\B-large.in"
output_file = r"F:\Nir\Downloads\sol2_large"

def is_increasing(s):
    return list(s) == sorted(s)

def solve2(num):
    if is_increasing(num):
        return num
    bad_digit = "x"
    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            bad_digit = num[i]
            break
    bad_idx = num.find(bad_digit)
    res = num[:bad_idx] + str(int(bad_digit)-1) + "9"*(len(num)-bad_idx-1)
    return str(int(res))




inp = open(filename, "r")
s = inp.read().split("\n")
inp.close()
res = ""

t = int(s[0])
for i, num in enumerate(s[1:-1]):
    res += "Case #{}: ".format(i+1) + solve2(num) + "\n"

out = open(output_file, "w")
out.write(res)
out.close()