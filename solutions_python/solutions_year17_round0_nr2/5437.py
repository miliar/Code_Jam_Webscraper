import os, time, sys, pprint
sys.setrecursionlimit(1800000)

cur_dir = os.path.dirname(os.path.abspath(__file__))
output = open(os.path.join(cur_dir, "tidy_output.txt"), "w")

print(cur_dir)

def log(msg):
	print(msg)
	output.write(str(msg) + "\n")

lines = []
for f in os.listdir(cur_dir):
	if f.lower().endswith("attempt0.in"):
		lines = open(os.path.join(cur_dir, f), "r").readlines()
		lines = [x.strip() for x in lines]
		break
# -----------------------------------------------------------------------------------
def is_tidy(num):
	return list(num) == sorted(num)

def find_lowest(num):
	for i in range(int(num), 0, -1):
		if is_tidy(str(i)):
			return i

# -----------------------------------------------------------------------------------

k = 0 
case = 1
num_cases = int(lines.pop(0))
while k < num_cases:
	num = lines[k]
	msg = find_lowest(num)
	log("Case #{}: ".format(case) + str(msg))
	k += 1
	
	case += 1

# print(is_tidy("123"))