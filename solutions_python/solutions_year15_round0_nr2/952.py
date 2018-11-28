from sys import stdin

def divide(x, n):
	if x % n == 0:
		return [x / n] * n

	result =  [x / n] * (n - 1)
	return result + [(x / n) + 1]


def handle_case(pancakes):
	max_pancakes = max(pancakes)
	if max_pancakes <= 3:
		return max_pancakes

	mod_pancakes = pancakes[:]
	mod_pancakes.remove(max_pancakes)
	return min(1 + handle_case(mod_pancakes + divide(max_pancakes, 2)), 
			   2 + handle_case(mod_pancakes + divide(max_pancakes, 3)), 
			   max_pancakes)

def main():
    for i in xrange(int(stdin.readline())):
        _ = stdin.readline()
        pancakes = [int(x) for x in stdin.readline().strip().split(" ")]
        print "Case #{}: {}".format(i + 1, handle_case(pancakes))


if __name__ == "__main__":
    main()