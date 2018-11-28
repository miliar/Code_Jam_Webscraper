import click
import math
import heapq

def choose(a, b):
	return math.floor((b + a) / 2)

def split(heap):
	_, a, b = heapq.heappop(heap)
	x = choose(a, b)
	heapq.heappush(heap, (a - (x - 1) - 1, a, x - 1))
	heapq.heappush(heap, (x + 1 - b - 1, x + 1, b))

@click.command()
@click.argument('filename')
def main(filename):
	f_in = open(filename)
	f_out = open(filename.replace('in', 'out'), 'w')
	T = int(f_in.readline())
	with click.progressbar(range(1, T + 1)) as bar:
		for T_iter in bar:
			N, K = [int(x) for x in f_in.readline().split()]
			heap = [(1-N-1, 1, N)]
			#print(heap)
			for k in range(1, K):
				split(heap)
				#print(heap)
				#if k > 2:
				#	break
			_, a, b, = heapq.heappop(heap)
			chosen = choose(a, b)
			z = min(chosen - a, b - chosen)
			y = max(chosen - a, b - chosen)
			f_out.write('Case #' + str(T_iter) + ': ' + str(y) + " " + str(z) + "\n")
			f_out.flush()
	f_in.close()
	f_out.close()
	
if __name__ == '__main__':
	main()