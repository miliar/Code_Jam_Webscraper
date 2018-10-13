
def ken_resp(nb, ken):
	for i in range(len(ken)):
		kb = ken[i]
		if kb > nb:
			return 0, ken[:i] + ken[i+1:]
	return 1, ken[1:]


def calc_war_score(N, naomi, ken):
	score = 0
	for nb in naomi:
		point, ken = ken_resp(nb, ken)
		score += point
	return score


def can_win_all(N, naomi, ken):
	assert len(naomi) == N and len(ken) == N
	for i in range(N):
		if ken[i] > naomi[i]:
			return False
	return True


def calc_dec_war_score(N, naomi, ken):
	for i in range(N):
		if can_win_all(N, naomi, ken):
			return N
		N -= 1
		naomi = naomi[1:]
		ken = ken[:-1]
	return 0


def calc_dw_and_w_scores(N, naomi, ken):
	naomi.sort()
	ken.sort()
	return calc_dec_war_score(N, naomi[:], ken[:]), calc_war_score(N, naomi[:], ken[:])


def read_int(f):
	return int(f.readline().strip())

def read_ints(f):
	return [int(w) for w in f.readline().strip().split()]

def read_floats(f):
	return [float(w) for w in f.readline().strip().split()]

def semi_float(s):
	ip, fp = s.split('.')
	while len(fp) < 5:
		fp = fp + '0'
	ip = int(ip)
	fp = int(fp)
	assert ip == 0
	return fp

def read_semi_floats(f):
	return [semi_float(w) for w in f.readline().strip().split()]

from sys import argv


in_f = open(argv[1])

T = read_int(in_f)

for i_t in range(1, T+1):
	N = read_int(in_f)
	naomi = read_semi_floats(in_f)
	ken = read_semi_floats(in_f)
	dw_score, w_score = calc_dw_and_w_scores(N, naomi, ken)
	print 'Case #%s: %s %s' % (i_t, dw_score, w_score)
