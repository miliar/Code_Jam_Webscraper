def main(filepath):
	f = open(filepath, 'r')
	out = open('cookie_farm_out.txt', 'w')
	num_cases = int(f.readline())
	for i in range(num_cases):
		secs = min_seconds(*(map(float, f.readline().split())))
		out.write('Case #%d: %.7f' % ((i+1), secs))
		if i < num_cases - 1:
			out.write('\n')

def min_seconds(C, F, X):
	time_to_get_farms = dict()
	time_to_get_farms[0] = 0
	def seconds_to_get_farms(num_farms):
		if num_farms in time_to_get_farms:
			return time_to_get_farms[num_farms]
		else:
			time = seconds_to_get_farms(num_farms-1) + C/(2+F*(num_farms-1))
			time_to_get_farms[num_farms] = time
			return time

	def seconds_for_fixed_farms(num_farms):
		return seconds_to_get_farms(num_farms) + X/(2+F*(num_farms))

	secs = seconds_for_fixed_farms(0)
	i = 1
	cont = True
	while cont:
		new_secs = seconds_for_fixed_farms(i)
		secs, cont = min(secs, new_secs), (new_secs <= secs)
		i += 1
	return secs

main('B-large.in')