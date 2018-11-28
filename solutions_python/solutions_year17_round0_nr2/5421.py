T = int(raw_input())
lst = []
count = 0

def non_decreasing(L):
    return all(x<=y for x, y in zip(L, L[1:]))

for i in range(T):
	lst.append(raw_input())

for itm in lst:
	new_itm = map(int, list(itm))
	if len(new_itm) == 1:
		print "Case #{}: {} ".format(lst.index(itm)+1, new_itm[0])
	elif non_decreasing(new_itm):
		print "Case #{}: {} ".format(lst.index(itm)+1, str(int(filter(str.isdigit, repr(new_itm)))))
	else:
		for j in range(1,len(new_itm)):
			if new_itm[j-1] >= new_itm[j]:
				new_itm[j-1] = new_itm[j-1]-1
				new_itm[j:] = [9]*(len(new_itm)-j)
				print "Case #{}: {} ".format(lst.index(itm)+1, str(int(filter(str.isdigit, repr(new_itm)))))
				break
		# else:
		# 	count = count +1
		# 	print "Case #{}: {} ".format(count, str(int(filter(str.isdigit, repr(new_itm)))))
		# 	break


# https://www.youtube.com/watch?v=hKrzFYVyeYw
