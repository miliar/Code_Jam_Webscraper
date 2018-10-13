"""
x = farm_price
y = farm_cps
z = win_limit

w = farm_count (planned farm count)
k = farms (current farm count)

final_cps   = (2 + farm_count * farm_cps)
            = 2+w*y
current_cps = (2 + farms * farm_cps)
            = 2+k*y

current_farm_time = farm_price / current_cps
                  = farm_price / (2 + farms * farm_cps)
	          = x/(2+k*y)
total_farm_time   = sum[farms=0..farm_count-1](current_farm_time)
                  = sum[farms=0..farm_count-1](farm_price / (2 + farms * farm_cps))
	          = sum[k=0..w-1](x/(2+k*y))

cookie_time = win_limit / final_cps
            = z/(2+w*y)

time = total_farm_time + cookie_time
     = sum[farms=0..farm_count-1](farm_price / (2 + farms * farm_cps)) + win_limit / final_cps
     = sum[k=0..w-1](x/(2+k*y)) + z/(2+w*y)

What happens to time when we increase farm_count by one? It increases by:
time(farm_count + 1) - time(farm_count) = sum[k=0..w](x/(2+k*y)) + z/(2+w*y+y) - sum[k=0..w-1](x/(2+k*y)) - z/(2+w*y)
                                        = x/(2+w*y) + z/(2+w*y+y) - z/(2+w*y)

That is:
time_delta = farm_price/old_final_cps + win_limit/new_final_cps - win_limit/old_final_cps
           = total_farm_time_delta + cookie_time_delta

(cookie_time_delta is negative)

We add one new farm, which adds the farm_price/old_final_cps term,
the old cookie_time is wrong, so there's a -win_limit/old_final_cps term,
and finally we need the new cookie_time, so there's a win_limit/new_final_cps term.

We want time_delta to be negative to save time, so the extra time from buying the farm
should be less than we gain with the new higher final_cps. That is:
time_delta < 0
total_farm_time_delta + cookie_time_delta < 0
total_farm_time_delta < -cookie_time_delta
farm_price/old_final_cps < win_limit/old_final_cps - win_limit/new_final_cps
x/(2+w*y) < z/(2+w*y) - z/(2+w*y+y) | divide by (2+w*y)
x < z - z*(2+w*y)/(2+w*y+y) = z*y/(2+w*y+y)

That is, time_delta is negative as long as:
farm_price < win_limit * farm_cps / (2 + farm_count * farm_cps + farm_cps)

How does the time_delta behave as we increase the farm_count?
Well, the right side of the last equation always gets smaller as the farm_count increases.
That is, there's a point such that before it it's always better to buy, and after it it's never worth it.
So, when we hit that point, we can stop, since the time isn't going to get any better later.

So, where is that damn point, then?
x = z*y/(2+w*y+y)
x*2+x*w*y+x*y = z*y
x*w*y = z*y-x*y-2*x
w = (z*y-x*y-2*x)/(x*y)
w = z/x-2/y-1

(but since we had time_delta = time(w+1) - time(w), it's really w+1)

So, the number of farms you should buy is:
farm_count = (win_limit*farm_cps - farm_price*farm_cps - 2*farm_price)/(farm_price*farm_cps) + 1
           = win_limit/farm_price - 2/farm_cps

(rounded down, since the next higher one would add more time)

"""
import sys

base_cps = 2

with open(sys.argv[1], 'r') as f:
	cases = int(f.readline().strip())
	for case in range(cases):
		farm_price, farm_cps, win_limit = map(float, f.readline().split())

		# Better safe than sorry: Calculate in two different ways and cross-check the answers

		cps = base_cps
		farms_took = 0
		last_took = farms_took + win_limit / cps
		last_farms = 0
		#print(0, farms_took, win_limit / cps, cps, last_took)
		max_farms = int(win_limit / farm_price) + 1
		for farm in range(max_farms):
			farms_took += farm_price / cps
			cps += farm_cps
			this_took = farms_took + win_limit / cps
			#print(farm + 1, farms_took, win_limit / cps, cps, this_took)
			if this_took > last_took:
				break
			last_took = this_took
			last_farms = farm + 1

		farm_count = max(int(win_limit/farm_price - 2/farm_cps), 0)
		took = sum(farm_price / (2 + farms * farm_cps) for farms in range(farm_count)[::-1]) + win_limit / (2 + farm_count * farm_cps)

		assert farm_count == last_farms
		assert abs(took - last_took) < 10**-6

		print('Case #%d: %.7f' % (case + 1, took))

