#python3.4

# so the idea is that buying a farm
# is better iff the buyer can reach the
# same level of 'cookieness' as the non-buyer
# before they finish. Observe that
#    (cps + F)*t = C + cps*t
# => F*t = C
# => t = C/F
# which means that C/F seconds pass
# before the buyer and non-buyer
# have the same amount of cookies.
# Thus, because algebra, the non-buyer
# will have C + cps*(C/F) cookies when
# the buyer will zoom past him with
# his glorious cookie farm. If this number
# is less than the target goal X of
# cookies, the player should not buy.

for N in range(int(input())):
	print("Case #%d: " % (N+1), end="")
	C, F, X = [float(n) for n in input().split()]
	cps = 2.0  # cookies per second
	# special case: cost of a farm is greater than goal,
	#               only a special case because of how
	#               I implemented the inner loop
	if C > X:
		print("%f" % (X/cps))
		continue
	cookies = 0.0  # total cookies
	time = 0.0  # time taken
	while True:
		# gain the equivalent of a farm
		cookies = C
		time += C/cps
		if (cookies + cps*C/F) < X:
			# buy a farm
			cookies = 0.0
			cps += F
		else:
			# just farm to the goal!
			print("%f" % (time + (X - cookies)/cps))
			break

