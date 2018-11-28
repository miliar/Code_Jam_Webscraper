def take_horse():
	pos, speed = map(int, input().split())
	return (pos, speed)


for sloni in range(int(input())):
	dest, n = map(int, input().split())
	horses = [take_horse() for _ in range(n)]
	etas = map(lambda x: (dest-x[0]) / x[1], horses) #sorted(horses, key=lambda x: -x[0])
	print("Case #%d: %f" % (sloni+1, dest/max(etas)))