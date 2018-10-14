T = int(raw_input())
for i in range(0,T):
	A = map(int,raw_input().split())
	armin_mote = A[0]
	M = map(int,raw_input().split())
	# print M, armin_mote
	M.sort()
	armin_sum = armin_mote
	operation_count = 0
	while len(M) > 0:
		pop_mote = M[0]
		if armin_sum > pop_mote:
			armin_sum += pop_mote
			del(M[0])
		else:
			o_armin_sum = armin_sum	
			armin_sum += (armin_sum-1)
			if armin_sum > pop_mote:
				armin_sum += pop_mote
				del(M[0])
				operation_count += 1
			else:
				tmp_count = 0
				t_armin_sum = o_armin_sum
				while t_armin_sum <= pop_mote:
					tmp_count += 1
					t_armin_sum += (t_armin_sum-1)
					if tmp_count > len(M):
						break
				if tmp_count >= len(M):
					operation_count += len(M)
					break
				else:
					armin_sum = t_armin_sum + pop_mote
					operation_count += (tmp_count)
					del(M[0])
	print "Case #%d: %d"%(i+1,operation_count)
	