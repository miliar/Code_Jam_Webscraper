def is_pancake(pancake):
	if "-" in pancake:
		return False
	return True

def flip_pancake(side):
	if (side == "-"):
		return "+"
	if (side == "+"):
		return "-"

count = 0
ncases = 0
file_object = open("large.input1", "r")
with open('output1.txt', 'w') as out:
    for line in file_object:
        flips = 0
        if (count == 0):
            count += 1
            ncases = int(line)
            continue
        pancake = line.replace("\n","")
        k       = int(pancake.split(' ')[1])
        pancake_list = list(pancake.split(' ')[0])
        try:
            for i in xrange(len(pancake_list)):
                if pancake_list[i] == "-":
                    flips += 1
                    for j in xrange(i,i + k):
                        pancake_list[j] = flip_pancake(pancake_list[j])
            if (is_pancake(''.join(pancake_list))):
                print("Case #{}: {}".format(count, flips))
                out.write("Case #{}: {}".format(count, flips))
                out.write('\n')
            else:
                print("Case #{}: {}".format(count, "IMPOSSIBLE"))
                out.write("Case #{}: {}".format(count, "IMPOSSIBLE"))
                out.write('\n')
            count += 1
        except:
            print("Case #{}: {}".format(count, "IMPOSSIBLE"))
            out.write("Case #{}: {}".format(count, "IMPOSSIBLE"))
            out.write('\n')
            count += 1
out.closed            
