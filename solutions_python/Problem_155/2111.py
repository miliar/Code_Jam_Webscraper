import timeit
start = timeit.default_timer()

def calculate(r,tempcount):
	temp_list = r.split()
	count = 0
	act_count = 0
	level = 0
	#t = int(temp_list[0]) + 1
	for x in temp_list[1]:
		if count < level:
			act_count = act_count + (level - count)
			count = count + (level - count)
		count = count + int(x)
		level = level + 1
	logfile = open('output.txt', 'a')
	logfile.write('Case #%s: %s\r\n' % (tempcount,act_count))
	logfile.close()

	#for i in tlist:
		#tj = (tlist.index(i) + 1)
		#clist = tlist[tj:]
		#for t in clist
		#temp = credit - tmax
		#if credit - i in clist:
			#tn = clist.index(credit - i) + tj +1
			#del tlist[tlist.index(tmax)]
			#tu = tlist.index(temp)+1
			#del tlist[tlist.index(temp)]
			#logfile = open('output.txt', 'a')
			#logfile.write('Case #%s: %s %s\r\n' % (tempcount,tj, tn))
			#logfile.close()
			#print 'Case #%s: %s %s' % (tempcount,tlist.index(i)+1, tlist.index(temp)+1)
			#clist.remove(i)
			#break

fname = 'simput.txt'
with open(fname) as f:
    content = f.readlines()
count = 0
tempcount = 1
logfile = open('output.txt', 'w')
logfile.write('')
logfile.close()

for r in content:
	if count == 0:
		pass
	else:
		calculate(r,tempcount)
		tempcount = tempcount + 1
	count = count + 1
stop = timeit.default_timer()
print stop - start