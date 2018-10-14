file = open('170408a_out0.txt', 'w')
def printp(*args, **kwargs):
	kwargs['file'] = file
	print(*args, **kwargs)
for _ in range(int(input())):
	printp('Case #{}:'.format(_+1), end=' ')
	k = input().split()
	pan = list(map(lambda x: int(x == '+'), k[0]))
	k = int(k[1])
	try:
		for counter in range(1000000):
			nach = pan.index(0)
			for huj in range(nach, nach+k):
				pan[huj] ^= 1
	except ValueError:
		printp(counter)
	except IndexError:
		printp('IMPOSSIBLE')
	except Exception as msg:
		print(msg)
file.close()