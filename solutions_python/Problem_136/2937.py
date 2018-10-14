#!/usr/bin/python3

def main():
	f = open('../test_files/input', 'r')
	w = open('../test_files/output', 'w')
	t = int(f.readline())
	for i in range(1, t+1):
		w.write('Case #%d: ' % i)

		c, u, x = [float(x) for x in f.readline()[:-1].split()]
		speed = 2
		time = 0
		while True:
			if x / speed > c / speed + x / (speed + u):
				time += c / speed
				speed += u
			else:
				w.write(str(time + x / speed) + "\n")
				break

	w.close()

if __name__ == '__main__':
	main()