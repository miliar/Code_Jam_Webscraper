
import sys

def t_process():
	n1 = int(sys.stdin.readline())
	n1 -= 1
	n1_matrix = [set(map(int, sys.stdin.readline().split())) for _ in range(4)]
	n2 = int(sys.stdin.readline())
	n2 -= 1
	n2_matrix = [set(map(int, sys.stdin.readline().split())) for _ in range(4)]
	sol = list(n1_matrix[n1].intersection(n2_matrix[n2]))
	if len(sol) > 1:
		return "Bad magician!"
	if len(sol) == 0:
		return "Volunteer cheated!"
	if len(sol) == 1:
		return int(sol[0])


def main():
	t = int(sys.stdin.readline())
	for k in range(1, t + 1):
		print("Case #{0}: {1}".format(k, t_process()))

main()

