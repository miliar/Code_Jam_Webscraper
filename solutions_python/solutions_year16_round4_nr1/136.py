import sys

def search(x, y, z, curr_level):
	global N, R, P, S, final, curr
	if (x > R or y > P or z > S):
		return "IMPOSSIBLE"
	if (curr_level == N):
		final = curr
		return "FINAL"
	curr = curr.replace("RS", "1")
	curr = curr.replace("PS", "2")
	curr = curr.replace("PR", "3")
	curr = curr.replace("1", "PSRS")
	curr = curr.replace("2", "PRPS")
	curr = curr.replace("3", "PRRS")
	return search(x + y, y + z, z + x, curr_level + 1)


def solve():
	global N, R, P, S, final, curr
	input_s = raw_input().split(" ")
	N = int(input_s[0])
	R = int(input_s[1])
	P = int(input_s[2])
	S = int(input_s[3])
	final = ""
	curr = "PR"
	if (search(1, 1, 0, 1) == "FINAL"):
		return final
	curr = "PS"
	if (search(0, 1, 1, 1) == "FINAL"):
		return final
	curr = "RS"
	if (search(1, 0, 1, 1) == "FINAL"):
		return final
	return "IMPOSSIBLE"

T = int(raw_input())
for i in range(T):
    print "Case #{}: {}".format(i + 1, solve())
