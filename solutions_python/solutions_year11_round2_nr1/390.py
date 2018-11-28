inp = file("input")
T = int(inp.readline())
out = file("output", "w")
case = 0

def WP(line):
	played = 0.0
	won = 0.0
	for l in line:
		if l != '.':
			played += 1.0
			if l == '1':
				won += 1.0
	if played == 0:
		return 0.0
	return won/played

def OWP(m, i):
	l = 0
	s_wps = 0
	t = 0
	while l < len(m):
		if l != i and m[i][l] != '.':
			line = ''
			letter = 0
			while letter < len(m[l]):
				if letter != i:
					line += m[l][letter]
				letter += 1
			s_wps += WP(line)
			t += 1
		l += 1
	if t == 0:
		return 0.0
	return s_wps/t	

def OOWP(OWPs, m, i):
	l = 0
	s_owps = 0
	t = 0
	while l < len(m):
		if l != i and m[i][l] != '.':
			s_owps += OWPs[l]
			t += 1
		l += 1
	if t == 0:
		return 0.0
	return s_owps/t

def RPI(wp, owp, oowp):
	return 0.25*wp + 0.5*owp + 0.25*oowp

while case < T:
	case += 1
	N = int(inp.readline())
	WPs = N*[None]
	OWPs = N*[None]
	OOWPs = N*[None]
	m = []
	for i in xrange(N):
		line = inp.readline()
		line = line.strip()
		m.append(line)
	for i in xrange(N):
		WPs[i] = WP(m[i])
		OWPs[i] = OWP(m,i)
	for i in xrange(N):
		OOWPs[i] = OOWP(OWPs, m ,i)

	out.write("Case #" + str(case) + ":\n")

	for i in xrange(N):
		out.write(str(RPI(WPs[i], OWPs[i], OOWPs[i])) + "\n")
