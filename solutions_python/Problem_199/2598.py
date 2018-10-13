import click

def flip(S, i, K):
	S = list(S)
	for j in range(0, K):
		S[i + j] = '+' if S[i + j] == '-' else '-'
	return ''.join(S)

@click.command()
@click.argument('filename')
def main(filename):
	f_in = open(filename)
	f_out = open(filename.replace('in', 'out'), 'w')
	T = int(f_in.readline())
	with click.progressbar(range(1, T + 1)) as bar:
		for T_iter in bar:
			S, K = f_in.readline().split()
			K = int(K)
			n = 0
			for i in range(0, len(S) - K + 1):
				if S[i] == '-':
					S = flip(S, i, K)
					n = n + 1
			out = 'IMPOSSIBLE' if '-' in S else str(n)				
			f_out.write('Case #' + str(T_iter) + ': ' + out + "\n")
			f_out.flush()
	f_in.close()
	f_out.close()
	
if __name__ == '__main__':
	main()