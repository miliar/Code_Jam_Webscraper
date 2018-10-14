from __future__ import division
import sys

def do_line(line):
	n, p_d, p_g = map(int, line.split(' '))
	print n, p_d, p_g

	pos_values = []
	for won in range(0,n+1):
		for lost in range(0,n+1-won):
			if won == 0 and lost == 0:
				continue
			if won * 100 / (won+lost) == p_d:
				pos_values.append((won, lost))
	still_pos = []
	try:
		for won, lost in pos_values:
			for total_won in range(won, (won+lost)*101):
				for total_lost in range(lost, (won+lost)*101):
					if total_won * 100 / (total_won + total_lost) == p_g:
						still_pos.append((total_won, total_lost, won, lost))
						throw
	except:
		pass
				
	for t_w, t_l, w, l in still_pos:
		print "Today: %d/%d (%f) Total: %d/%d (%f)" % (w,w+l, w/(w+l)*100, t_w, (t_w+t_l), t_w/(t_w+t_l)*100)
	
	if len(still_pos) > 0:
		return "Possible"
	else:
		return "Broken"



in_, out_f= sys.argv[1], sys.argv[1]+".out"
out = open(out_f, 'w')
with open(in_, 'r') as file:
	file.next()
	num = 1
	for line in file:
		ret = do_line(line)
		out.write("Case #%d: %s\n" % (num, ret))
		num += 1

