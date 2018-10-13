f = open("cruiseControlLarge.in", "r")
new_file = open("cruiseControlLargeSol", "w")
t = int(f.readline())

def max_cruising_speed(d, kisi):
	smallest_cruising_speed = 100000000000000
	for ki, si in kisi:
		multiplier = float(d)/(d-ki)
		speed = multiplier * si
		smallest_cruising_speed = min(speed, smallest_cruising_speed)
	return smallest_cruising_speed



for i in range(1,t+1):
	d, n = [int(x) for x in f.readline().split(' ')]
	kisi = []
	for j in range(n):
		ki, si = [int(x) for x in f.readline().split(' ')]
		kisi.append((ki,si))
	new_file.write("Case #"+str(i)+ ": "+str(max_cruising_speed(d, kisi))+"\n")