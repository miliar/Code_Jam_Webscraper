
import argparse

def solve():
	pass

def main(f_in, f_out):

	t = int(f_in.readline().strip())
	for case in range(1, t+1):
		d, n = f_in.readline().strip().split()
		d = int(d)
		n = int(n)
		horses = []
		for r in range(n):
			k, s = f_in.readline().strip().split()
			horses.append([int(k), int(s)])

		sorted_horses = sorted(horses, key=lambda x: x[0], reverse=True)

		print(sorted_horses)

		max_time = 0
		for h in sorted_horses:
			time = (d - h[0] * 1.0)/h[1]
			max_time = max(max_time, time)

		solution = d * 1.0 / max_time
		f_out.write('Case #{}: {:.8f}\n'.format(case, solution))

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('infile')

	opts = parser.parse_args()
	infile = opts.infile

	outfile = infile.split('.')[0]+'.out'

	with open(infile, 'r') as f_in:
		with open(outfile, 'w') as f_out:
			main(f_in, f_out)