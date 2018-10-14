
def doit(i, N, K):
	N = 2**N-1;
	if K > N+1:
		K = K % (N+1);
	if K == N:
		print("Case #" + str(i) + ": ON");
	else:
		print("Case #" + str(i) + ": OFF");

def main():
	c = input();
	i = 1;
	while i <= int(c):
		str = input();
		lst = str.split();
		doit(i, int(lst[0]), int(lst[1]));
		i = i + 1;
	
main();
