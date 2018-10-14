file = open('170422a_outest.txt', 'w')
def printp(*args, **kwargs):
	kwargs['file'] = file
	print(*args, **kwargs)
for _ in range(int(input())):
	d, n = map(int, input().split())
	t = 0
	for __ in range(n):
		k, s = map(int, input().split())
		t = max(t, (d-k)/s)
	printp('Case #{}:'.format(_+1), d/t)
file.close()