
def B(n):
	for num in range(n,0,-1):
		l=list(str(num))
		if l == list(sorted(l)):
			return num

if __name__ == '__main__':
	with open("input.txt") as f:
		a = f.readlines()
		for i in range(int(a[0])):
			print(f"Case #{i+1}: {B(int(a[i+1]))}", file=open("out.txt", "a"))
