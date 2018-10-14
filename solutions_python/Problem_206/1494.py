

cases = int(input())

res = []

for case in range(cases):
	destination, horses = input().split(' ')
	destination = int(destination)
	horses = int(horses)
	max_speed = 10001
	last_tmp_res = 0
	for i in range(horses):
		destination_2 = destination
		tmp_1, tmp_2 = input().split(' ')
		tmp_1 = int(tmp_1)
		tmp_2 = int(tmp_2)
		tmp_res = (destination_2 - tmp_1)
		tmp_res /= tmp_2
		destination_2 /= tmp_res
		
		if last_tmp_res == 0 or destination_2<last_tmp_res:
			last_tmp_res = destination_2
	res.append(last_tmp_res)
		
for pos, i in enumerate(res, start=1):
	print('Case #{}: {:.6f}'.format(pos, i))