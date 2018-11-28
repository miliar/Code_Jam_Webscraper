from sets import Set

def main():
	for t in range(1, int(raw_input()) + 1):
		a = int(raw_input())
		elemA = [[] for i in range(4)]
		for i in range(4):
			elemA[i] = map(int, raw_input().strip().split(' '))

		b = int(raw_input())
		elemB = [[] for i in range(4)]
		for i in range(4):
			elemB[i] = map(int, raw_input().strip().split(' '))

		result = list(Set(elemA[a - 1]).intersection(Set(elemB[b - 1])))
		if len(result) == 1:
			print("Case #" + str(t) + ": " + str(result[0]))
		elif len(result) > 1:
			print("Case #" + str(t) + ": Bad magician!")
		else:
			print("Case #" + str(t) + ": Volunteer cheated!")


if __name__ == '__main__':
	main()