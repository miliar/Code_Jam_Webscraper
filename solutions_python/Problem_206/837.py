import sys
import math

T = int(input())

for t in range(T):
	res = 0.0
	line = list(map(int,input().split()))
	annies_d, n_horses = line[0], line[1]
	time_to_destination = list()
	for n in range(n_horses):
		line = list(map(int,input().split()))
		horse_km, horse_vel = line[0], line[1]
		time_to_destination.append((annies_d-horse_km)/horse_vel)
	slowest_horse = max(time_to_destination)
	res = annies_d/slowest_horse
	print('Case #{0}: {1:.6f}'.format(t+1, res))