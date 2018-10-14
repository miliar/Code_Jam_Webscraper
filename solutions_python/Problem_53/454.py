# Hey hey! A line of snappers is like a binary number.
# Snapping is like adding one to that number.
# Going over 2**N resets the number.
# The light is on if all the digits are 1, or if K == 2**N - 1

def solve(N, K, case):
    out = "Case #" + str(case+1) + ": "
    K = K % 2**N
    if K == 2**N - 1:
       out += "ON"
    else:
        out += "OFF"
    return out


f = open("A-large.in", "r")
out = ""

T = int(f.readline().strip())
for case in range(T):
    line = f.readline().split()
    N = int(line[0].strip())
    K = int(line[1].strip())
    out += solve(N, K, case) + "\n"

f = open("output.txt", "w")
f.write(out)
f.close()
