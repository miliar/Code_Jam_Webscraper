import sys

def solve(number_special, focus_score, scores):
    count = number_special
    num = 0
    min_score = focus_score - 2
    if min_score < 0:
        min_score = 0
    min_value = focus_score + (min_score)*2
    surprise_value = focus_score*3 - 3
    for score in scores:
        if int(score) < min_value:
            continue
        elif int(score) <= surprise_value:
            if count > 0:
                count -= 1
                num += 1
            else:
                continue
        else:
            num += 1
    return num

if __name__ == "__main__":

	f = open('B-large.in.txt', 'r')
	g = open('B.out', 'w')
	count = int(f.readline())
	for i in xrange(int(count)):
		case = f.readline().strip().split()
		result = solve(int(case[1]), int(case[2]), case[3:])
		r = "Case #" + str(i+1) +  ": " + str(result)
		print r
		if (i != count-1):
			r = r + '\n'
		g.write(r)