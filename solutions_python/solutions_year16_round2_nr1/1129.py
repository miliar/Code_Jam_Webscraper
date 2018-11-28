


def solve(s):
	orig = s
	NUMBERS = ['SIX', 'ZERO', 'EIGHT', 'TWO', 'FOUR', 'FIVE', 'SEVEN', 'NINE', 'ONE', 'THREE', ]
	word_to_digit = {'ZERO':'0', 'ONE':'1', 'TWO':'2', 'THREE':'3', 'FOUR':'4', 'FIVE':'5', 'SIX':'6', 'SEVEN':'7', 'EIGHT':'8', 'NINE':'9'}
	phone = ''

	j = 0
	while j < len(NUMBERS):
		num = NUMBERS[j]
		cache = s
		i = 0
		streak = True
		while i < len(num) and streak:
			if num[i] in cache:
				cache = cache.replace(num[i], '', 1)
				i += 1
			else:
				streak = False
		if streak:
			s = cache
			phone += word_to_digit[num]
		if not streak:
			j += 1

	if len(cache) > 0:
		print orig, cache

	ans = ''.join(sorted(phone))
	return ''.join(ans)


def rotate(l,n):
    return l[n:] + l[:n]


def main():
	r = open('input_file.txt', 'r')
	w = open('output_file.txt', 'w')

	t = int(r.readline())
	for i in xrange(1, t + 1):
		s = r.readline().strip()
		w.write('Case #{}: {}\n'.format(i, solve(s)))


main()