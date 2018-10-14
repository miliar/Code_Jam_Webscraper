#!/usr/bin/python
filename = "sample.in";
filename = "A-small-attempt0.in";
filename = "A-large.in";
data_sets = [line.strip() for line in open(filename,'r').readlines()[1:]]
data_sets = [data_sets[i:i+4] for i in xrange(0,len(data_sets),5)];
case = 1;
for data_set in data_sets:
	data_set = map(list,data_set);
	for column in zip(*data_set):
		 data_set.append(list(column));
	data_set.append([]);
	data_set.append([]);
	for i in xrange(4):
		data_set[-2].append(data_set[i][i]);
		data_set[-1].append(data_set[3-i][i]);
		
	xwin = False;
	owin = False;
	gameFinished = True;
	for row in data_set:
		xcount = row.count('X');
		tcount = row.count('T');
		ocount = row.count('O');
		if(gameFinished):
			if '.' in row:
				gameFinished = False;
		xwin = (xwin or xcount+tcount == 4);
		owin = (owin or ocount+tcount == 4);
	if ( xwin ):
		caseString = "X won";
	elif ( owin ):
		caseString = "O won";
	elif ( gameFinished ):
		caseString = "Draw";
	else: 
		caseString = "Game has not completed";
	print "Case #" + str(case) + ": " + caseString;
	case+=1;
	

