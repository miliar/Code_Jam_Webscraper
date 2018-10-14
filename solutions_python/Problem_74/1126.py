import sys


def get_next_token (ip, cnt):
	num = ''
	while ip [cnt] == ' ':
		cnt += 1
	bot = ip [cnt]
	cnt += 2
	while cnt < len (ip) and ip [cnt] != ' ':
		num += ip [cnt]
		cnt += 1
	return (bot.lower (), int (num), cnt)


def solve (ip):
	secs = 0
	cnt = 0
	while ip [cnt] != ' ':
		cnt += 1
	cnt += 1
	ip = ip [cnt:]
	
	o_last = 1
	b_last = 1

	o_delt = 0
	b_delt = 0

	first = True
	prev_bot = None

	cnt = 0
	while True:
		#print >> sys.stderr, cnt, ip
		bot, switch, cnt = get_next_token (ip, cnt)
		#print >> sys.stderr, bot, switch, cnt
		if prev_bot == bot:
			exec bot + '_delt = 0'
		diff = abs (eval ('switch - ' + bot + '_last'))
		time = eval ( 'diff + 1 - ' + bot + '_delt')
		if time <= 0:
			time = 1
		if bot == prev_bot:
			if bot == 'o':
				b_delt += time
			else:
				o_delt += time
		else:
			if bot == 'o':
				b_delt = time
			else:
				o_delt = time
		secs += time
		exec bot + '_last = switch'
		#print >> sys.stderr, "bot :", bot, "time :", time, "secs :", secs
		prev_bot = bot
		if cnt >= len (ip):
			break
	return secs




def main ():
	r = open ("bot_in_large")
	w = open ("bot_op_large", "w+")
	t = r.readline ()
	cnt = 0
	for case in r.readlines ():
		cnt += 1
		w.write ("Case #%d: %d\n" %(cnt, solve (case)))
	w.close ()
	r.close ()

main ()
