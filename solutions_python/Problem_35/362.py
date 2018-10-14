#!/usr/bin/python

label=ord('a')

def find_sink(x,y):
	global label
	if(map[x][y][1]!=0):
		return map[x][y][1];
	lowest=map[x][y][0];
	place=(x,y);

	if(map[x-1][y][0]<lowest):
		lowest=map[x-1][y][0];
		place=(x-1,y);
	if (map[x][y-1][0]<lowest):
		lowest=map[x][y-1][0];
		place=(x,y-1);
	if (map[x][y+1][0]<lowest):
		lowest=map[x][y+1][0];
		place=(x,y+1);
	if(map[x+1][y][0]<lowest):
		lowest=map[x+1][y][0];
		place=(x+1,y);

	if(place==(x,y)):
		#This is a sink, label it and return the label
		map[x][y][1]=label;
		label+=1;
	else:
		#Get the label of our downstream fellow
		map[x][y][1]=find_sink(place[0],place[1]);

	return map[x][y][1];

f=open("maps.txt");

line=f.readline();

T=int(line);


for i in range(0,T):
	map=[];
	label=ord('a')
	size=f.readline().split();
	H=int(size[0]);
	W=int(size[1]);
	map.append([(999999,0)]*(W+2));
	for j in range(0,H):
		map.append([(999999,0)]);
		for c in f.readline().split()[:W]:
			map[-1].append([int(c),0]);
		map[-1].append([999999,0]);
	map.append([(999999,0)]*(W+2));
	for j in range(1,H+1):
		for k in range(1,W+1):
			if(map[j][k][1]==0):
				map[j][k][1]=find_sink(j,k);
	print "Case #"+str(i+1)+":"
	for j in range(1,H+1):
		print " ".join([ chr(l[1]) for l in map[j][1:W+1]])
