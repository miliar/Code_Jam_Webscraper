import click

@click.command()
@click.argument('filename')
def main(filename):
	f_in = open(filename)
	f_out = open(filename.replace('in', 'out'), 'w')
	T = int(f_in.readline())
	with click.progressbar(range(1, T + 1)) as bar:
		for T_iter in bar:
			N = int(f_in.readline())			
			out = str(N)
			for i in reversed(range(N + 1)):
				s = str(i)
				if (s == ''.join(sorted(s))):
					out = i
					break
			f_out.write('Case #' + str(T_iter) + ': ' + str(out) + "\n")
			f_out.flush()
	f_in.close()
	f_out.close()
	
if __name__ == '__main__':
	main()