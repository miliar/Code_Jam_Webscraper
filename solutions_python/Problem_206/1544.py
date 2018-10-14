# start at 0 km
# destination D km
# N other horses, travel forever, start between 0 and D (K_i) travelling S_i km/h

import sys
import collections

def horse_to_dest(km, speed, D):
	return (D-km)/speed


def run(D, N, horses):
	print(D)
	print(N)
	print(horses)
	
	horses_km = list(horses.keys())
	horses_speed = list(horses.values())
	
	if N == 1:
		k, v = horses.popitem()
		time = horse_to_dest(k, v, D)
		return D/time
	else:
		while len(horses) > 1:
			k1, s1 = horses.popitem()
			k2, s2 = horses.popitem()
			
			if s1 == s2:
				if k1 < k2:
					horses[k1] = s1
				else:
					horses[k2] = s2
				continue
			
			
			# time to "collision"
			time = (k2-k1)/(s1-s2)
			if time < 0:
				if s1 < s2:
					horses[k1] = s1
				else:
					horses[k2] = s2
				continue

			# collision point
			position = k1 + s1*time
			
			# collision point can be after D, then we only care about the horse with the smaller starting position
			if position >= D:
				if k1 < k2:
					horses[k1] = s1
				else:
					horses[k2] = s2
				continue
			
			# virtual distance to add calculated time again
			virtual_distance = - time * min(s1,s2)
			horses[position + virtual_distance] = min(s1,s2)

		return run(D, len(horses), horses)
						
		

with open(sys.argv[1]) as f:
	lines = f.readlines()

with open("outA.txt", "w") as f:
	i = 1
	c = 1
	while i < len(lines)-1:
		# first line
		arr = list(map(int, lines[i].split()))
		D = arr[0]
		N = arr[1]
		horses = collections.OrderedDict()
		i += 1
		# key: km, value: speed
		for j in range(1,N+1):			
			arr = list(map(int, lines[i].split()))
			horses[arr[0]] = arr[1]
			i += 1
		
		horses = collections.OrderedDict(sorted(horses.items(), key=lambda t: t[0]))
		
		res = run(D,N,horses)
		f.write("Case #{}: {}\n".format(c, round(res,6)))
		print("Case #{}: {}".format(c, round(res,6)))
		c += 1
