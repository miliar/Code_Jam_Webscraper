#!/usr/bin/python3

import math
from decimal import Decimal


def do_case():
	fC, fJ  = [int(s) for s in input().strip().split(" ")] 
	
	cam = []
	fCtime = 0;
	while fC>0:
		start, finish = [int(s) for s in input().strip().split(" ")];
		fCtime += finish-start;
		if len(cam)>0 and cam[-1][1] == start:
			cam[-1][1] = finish;
		else:
			cam.append([start, finish, "C"])
		fC -= 1;

	jam = []
	fJtime = 0;
	while fJ>0:
		start, finish = [int(s) for s in input().strip().split(" ")];
		fJtime += finish-start;
		if len(jam)>0 and jam[-1][1] == start:
			jam[-1][1] = finish;
		else:
			jam.append([start, finish, "J"])
		fJ -= 1;
	
	fC = len(cam);
	fJ = len(jam);
	
	if fC + fJ == 1:
		return 2;
	
	together = sorted(cam + jam, key= lambda x: x[1]);
	oC =0;
	oCtime = [];
	oJ =0;
	oJtime = [];
	for i in range(1, len(together)):
		if together[i][2] == together[i-1][2] == "C":
			oC += 1;
			oCtime.append(together[i][0] - together[i-1][1]);
		if together[i][2] == together[i-1][2] == "J":
			oJ += 1;
			oJtime.append(together[i][0] - together[i-1][1]);
	if together[0][2] == together[-1][2] == "C":
		if together[0][0] == 0 and together[-1][1] == 2*720:
			fC -= 1;
		else:
			oC += 1;
			oCtime.append(together[0][0] + 2*720-together[-1][1]);
	if together[0][2] == together[-1][2] == "J":
		if together[0][0] == 0 and together[-1][1] == 2*720:
			fJ -= 1;
		else:
			oJ += 1;
			oJtime.append(together[0][0] + 2*720-together[-1][1]);
	
	oCtime = sorted(oCtime);
	oJtime = sorted(oJtime);
	
	changes = fC + fJ - oC - oJ;
	
	while fCtime + sum(oCtime) > 720:
		changes += 2;
		oCtime.pop();
	while fJtime + sum(oJtime) > 720:
		changes += 2;
		oJtime.pop();
	return changes;

t = int(input());
for ti in range (1, t+1):
	print("Case #{}: {}".format(ti, do_case()));
	
