

def flip(faces):
	return map(lambda x: 0 if x == 1 else 1, faces)


def k_flips(faces, k):
	flips = 0
	i = 0
	while i < len(faces):
		if 0 == faces[i]:
			if len(faces[i:i+k]) != k:
				return 'IMPOSSIBLE'
			faces[i:i+k] = flip(faces[i:i+k])
			flips += 1
		i+=1
	return flips


with open('A-small-attempt0.in', 'r') as f_in:
	next(f_in)
	with open('output', 'w') as f_out:
		count = 1
		for line in f_in:
			parts = line.split(' ')
			k = int(parts[1])
			faces = map(lambda x: 1 if x == '+' else 0, parts[0])
			f_out.write('Case #{}: {}\n'.format(count, k_flips(faces, k)))
			count += 1

			




