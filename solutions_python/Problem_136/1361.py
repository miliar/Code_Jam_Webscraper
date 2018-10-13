
def compute_time(c, f, x):
	num_buy = 0
	t_win_prev = 0
	t_pur_prev = 0
	t_pur = 0
	t_win = 1000000
	total_time = 0
	while(True):
		t_win_prev = t_win
		t_pur_prev = t_pur
		t_win = float(x)/(2+num_buy*f)
		t_pur = float(c)/(2+num_buy*f)

		if t_pur_prev + t_win > t_win_prev:
			total_time += t_win_prev - t_pur_prev
			break
		else:
			total_time += t_pur
			num_buy += 1
	return total_time

def main():
	input_file = open('input.in','r')
	output_file = open('results.txt','w')
	lines = input_file.readlines()
	num_out = int(lines[0])
	for i in range(num_out):
		c, f, x = [float(a.strip()) for a in lines[i+1].strip().split(' ')]
		output_file.write('Case #'+str(i+1)+': '+ str(compute_time(c,f,x))+'\n')

if __name__ == '__main__':
	main()