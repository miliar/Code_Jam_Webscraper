# -*- coding: utf-8 -*-
fname = "A-large"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

numcases = gcj_read()[0]

for caseno in range(numcases):
    bits = fin.readline().strip().split()[1:]
    order = zip(*[iter(bits)]*2)
    print order
    pos = {'O':1, 'B':1}
    time = {'O':0, 'B': 0}
    Bpos, Btime = 0, 0
    Opos, Otime = 0, 0
    for bot, button in order:
	button = int(button)
	otherbot = 'O' if bot=='B' else 'B'
	movetime = abs(button-pos[bot])
	time[bot] = max(time[bot] + movetime, time[otherbot]) + 1 # +1 to push button
	pos[bot] = button
	print time
    
    totaltime = str(max(time['O'], time['B']))
    print totaltime
    
    fout.write("Case #"+str(caseno+1)+": "+ totaltime+"\n")

fin.close()
fout.close()
