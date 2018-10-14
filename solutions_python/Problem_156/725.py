# Problem C
import fileinput



def eat(plates, minute, max_min):
	if minute >= max_min:
		return minute
	e = [max(0, i - 1) for i in plates]
	if any(e):
		return min(eat(e, minute + 1, max_min), special(e, minute + 1, max_min))
	else:
		return minute

def special(plates, minute, max_min):
	if minute >= max_min:
		return minute
	e = list(plates)	
	i = max(enumerate(plates), key=lambda x:x[1])[0]
	if (e[i] == 9):
		d = e[i] // 2
		e[i] = e[i] - d
		e.append(d)
		d = 3
		e2 = list(plates)
		e2[i] = e2[i] - d
		e.append(d)
		return min(eat(e, minute + 1, max_min), special(e, minute + 1, max_min), eat(e2, minute + 1, max_min), special(e2, minute + 1, max_min))
	else:
		d = e[i] // 2
		e[i] = e[i] - d
		e.append(d)
		return min(eat(e, minute + 1, max_min), special(e, minute + 1, max_min))	

stdin = fileinput.input()
T = int(stdin.readline())
for ti in range(T):
	D = int(stdin.readline().strip())
	plates = list(map(int, stdin.readline().strip().split(' ')))
	max_m = max(plates)
	m = min(eat(plates, 1, max_m), special(plates, 1, max_m))
	print('Case #' + str(ti + 1) + ': ' + str(m))
