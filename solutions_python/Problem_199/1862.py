import sys

def flip_cake(cake):
    cake = cake.replace('-','0')
    cake = cake.replace('+','-')
    cake = cake.replace('0','+')
    return cake

def cake_flipper(cakes, k_size, flips):
    perfect = True
    for each in cakes:
        if(each == '-'):
            perfect = False
    if(perfect):
        return flips
    elif(len(cakes) < k_size):
        return 'IMPOSSIBLE'
    elif(cakes[0]=='+'):
        return cake_flipper(cakes[1:], k_size, flips)
    else:
        return cake_flipper(flip_cake(cakes[0:k_size])+cakes[k_size:], k_size, flips + 1)

def read_in():
	tests = sys.stdin.readline()
	counts = int(tests)
	for each in range(1,counts + 1):
		line = sys.stdin.readline()
		print('Case #' + str(each) + ':', cake_flipper(line.rstrip().split()[0], int(line.rstrip().split()[1]), 0))
def main():
	lines = read_in()
if __name__ == '__main__':
	main()