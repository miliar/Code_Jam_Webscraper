def solve(data):

	firstanswer = int(data[0])
	secondanswer = int(data[5])

	# print firstanswer, secondanswer

	a = [int(x) for x in data[firstanswer].split(" ")]
	b = [int(x) for x in data[5+secondanswer].split(" ")]

	common = [y for y in a if y in b]

	if len(common) == 1:
		return common[0]
	if len(common) == 0:
		return "Volunteer cheated!"
	if len(common) > 1:
		return "Bad magician!"

g = open("AA-out.txt","w")


f = open("AA-in.txt","r")
d = f.read().split("\n")
n = int(d[0])

j = 1
for i in range(n):
	t = d[j:j+10]
	j = j + 10
	ans = str(solve(t))
	g.write("Case #" + str(i+1) + ": " + ans + "\n")