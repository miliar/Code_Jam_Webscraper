def magic(a1, c1, a2, c2):
	possible1 = c1[a1 - 1]
	#print(possible1)
	possible2 = c2[a2 - 1]
	count = 0
	card = [0] * 16
	for i in range(4):
		for j in range(4):
			if possible1[i] == possible2[j]:
				count += 1
	if count == 1:
		for i in range(4):
			card[possible1[i] - 1] += 1
		for j in range(4):
			card[possible2[j] - 1] += 1
		a = card.index(2)
		ret = a + 1
		return ret
	if count == 0:
		return "Volunteer cheated!"
	if count > 1:
		return "Bad magician!"	

def main():
	num_tests = int(input())
	for i in range(1, num_tests + 1):
		a1 = int(input())
		c1 = []
		for j in range(4):
			temp = input().split(" ")
			int_temp = [int(x) for x in temp]
			c1.append(int_temp)
		a2 = int(input())
		c2 = []
		for j in range(4):
			temp = input().split(" ")
			int_temp = [int(x) for x in temp]
			c2.append(int_temp)

		print("Case #" + str(i) + ":" + " ", end="")
		print(magic(a1, c1, a2, c2))

if __name__ == "__main__":
	main()