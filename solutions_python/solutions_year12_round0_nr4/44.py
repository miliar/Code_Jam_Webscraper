# Tested and running on: 
# Python 2.7.2 (default, Jan 20 2012, 15:37:52) 
# [GCC 4.2.1 Compatible Apple Clang 3.0 (tags/Apple/clang-211.12)] on darwin

# (C) 2012 Dennis Bliefernicht

from math import *

EPS = 1e-10
TOL = 0.0001

class FoundHit(Exception):
	pass
	
def ismirr(room, x, y):
	return room[y][x] == '#'
	
def isme(room, x, y):
	return room[y][x] == 'X'

def vlen(v):
	return sqrt(v[0]*v[0] + v[1]*v[1])

def norm(v):
	f = vlen(v)
	if f != 0.0:
		return (v[0] / f, v[1] / f)
	else:
		return v

def appeq(v1, v2):
	if abs(v1[0] - v2[0]) <= EPS and abs(v1[1] - v2[1]) <= EPS:
		return True
	return False

def sgn(x):
	if x >= 0.0:
		return 1
	else:
		return -1

def process():
	(h, w, d) = map(lambda x: int(x), pop().split(" "))
	room = []
	
	
	for l in range(h):
		line = pop()
		room.append(line)
		if line.find('X') != -1:
			myx = float(line.index('X')) + 0.5
			myy = float(len(room) - 1) + 0.5
	
	SAMP = d * 1.0
	
	# prepare emission vectors
	vlist = []
	vblist = []
	for x in range(-int(SAMP), int(SAMP+1)):
		for y in range(-int(SAMP), int(SAMP+1)):
			if x == 0 and y == 0:
				continue

			v = norm( (x*1.0, y*1.0) )
			found = False
			for v2 in vlist:
				if appeq(v, v2):				
					found = True
					break
			
			if not found:
				vlist.append(v)
				
	vlist.sort()
						
	# run through each vector
	cnt = 0
	for vect in vlist:
		px = myx # current ray position
		py = myy
		v = vect # current ray vector
		l = d # travel length
		
		#raypath = "%f\t%f" % (px, py)
		#print "NEWRAY  !!!!!  restl = %f, p = (%f, %f), v = %s" % (l, px, py, str(v))
		while l >= 0:
			besthitpos = None
			besthitvec = None
			besthitdist = 10000000.0	
			besthitdestroy = False
					
			# check for collisions with mirrors
			wmin = 0
			wmax = w-1
			hmin = 0
			hmax = h-1

			if sgn(v[0]) >= 0:
				wmin = int(floor(px))
			else:
				wmax = int(ceil(px))
			if sgn(v[1]) >= 0:
				hmin = int(floor(py))
			else:
				hmax = int(ceil(py))
				
			if wmax > w-1:
				wmax = w-1
			if hmax > h-1:
				hmax = h-1
			for wtx in range(wmin, wmax+1):
				for wty in range(hmin, hmax+1):
					if not ismirr(room, wtx, wty):
						continue
						
					tdist = vlen( (px - wtx, py - wty) )
					if tdist > l + 2:
						continue

					#print "trying %d %d" %(wtx, wty)
					# collision with vertical walls
					if floor(px) != wtx and v[0] != 0:
						if px > wtx: # collision with right wall
							xwall = wtx + 1.0
						else: # collision with left wall
							xwall = wtx 
						
						s = (xwall - px) / v[0]
						#print "s = %f" % s
						if s > 0:
							ywall = py + s * v[1]
							#print "ywall = %f" % ywall
							if ywall + TOL >= wty and ywall - TOL <= (wty+1):
								# HIT!
								dist = vlen( (px - xwall, py - ywall) )
								#print "possible VHIT (%f, %f) with block %d, %d @ %f" % (xwall, ywall, wtx, wty, dist)
								if dist < l and dist < besthitdist:
									if abs(xwall - round(xwall)) < EPS and abs(ywall - round(ywall)) < EPS:
										# corner!
										# check if the ray collides with the block at all, vector needs same signum as vector from corner to block center
										#print "CORNER xywall = (%f, %f), wt = (%d, %d)!" % (xwall, ywall, wtx, wty)
										#print "   signums = %d %d %d %d" % (sgn(v[0]), sgn(wtx + 0.5 - xwall), sgn(v[1]), sgn(wty + 0.5 - ywall))
										if sgn(v[0]) == sgn(wtx + 0.5 - xwall) and sgn(v[1]) == sgn(wty + 0.5 - ywall):
											# ray hits block, have to check neighbours 
											neighx = False
											neighy = False
											if round(xwall) == wtx:
												if ismirr(room, wtx-1, wty):
													neighx = True
											else:
												if ismirr(room, wtx+1, wty):
													neighx = True
											if round(ywall) == wty:
												if ismirr(room, wtx, wty-1):
													neighy = True
											else:
												if ismirr(room, wtx, wty+1):
													neighy = True		
													
											#print "BLOCKHIT neighx = %s, neighy = %s" % (str(neighx), str(neighy))
											if neighx:
												if neighy:
													besthitdestroy = False
													besthitdist = dist
													besthitpos = (xwall, ywall)
													besthitvec = (-v[0], -v[1])
												else:
													besthitdestroy = False
													besthitdist = dist
													besthitpos = (xwall, ywall)
													besthitvec = (v[0], -v[1])
											else:
												if neighy:
													besthitdestroy = False
													besthitdist = dist
													besthitpos = (xwall, ywall)
													besthitvec = (-v[0], v[1])
												else:
													besthitdestroy = True
													besthitdist = dist
													besthitpos = (xwall, ywall)

									else:
										# hits the wall, reflect
										besthitdist = dist
										besthitpos = (xwall, ywall)
										besthitvec = (-v[0], v[1])
										besthitdestroy = False
									
					# collision with horizontal walls
					if floor(py) != wty and v[1] != 0:
						if py > wty: # collision with right wall
							ywall = wty + 1.0
						else: # collision with left wall
							ywall = wty 
						
						s = (ywall - py) / v[1]
						if s > 0:
							xwall = px + s * v[0]
							if xwall + TOL >= wtx and xwall - TOL <= (wtx+1):
								# HIT!
								dist = vlen( (px - xwall, py - ywall) )
								#print "possible HHIT (%f, %f) with block %d, %d @ %f" % (xwall, ywall, wtx, wty, dist)
								if dist < l and dist < besthitdist:
									if abs(xwall - round(xwall)) < EPS and abs(ywall - round(ywall)) < EPS:
										# corner!
										# check if the ray collides with the block at all, vector needs same signum as vector from corner to block center
										#print "CORNER xywall = (%f, %f), wt = (%d, %d)!" % (xwall, ywall, wtx, wty)
										#print "   signums = %d %d %d %d" % (sgn(v[0]), sgn(wtx + 0.5 - xwall), sgn(v[1]), sgn(wty + 0.5 - ywall))
										if sgn(v[0]) == sgn(wtx + 0.5 - xwall) and sgn(v[1]) == sgn(wty + 0.5 - ywall):
											# ray hits block, have to check neighbours 
											neighx = False
											neighy = False
											if round(xwall) == wtx:
												if ismirr(room, wtx-1, wty):
													neighx = True
											else:
												if ismirr(room, wtx+1, wty):
													neighx = True
											if round(ywall) == wty:
												if ismirr(room, wtx, wty-1):
													neighy = True
											else:
												if ismirr(room, wtx, wty+1):
													neighy = True		
													
											#print "BLOCKHIT neighx = %s, neighy = %s" % (str(neighx), str(neighy))
											if neighx:
												if neighy:
													besthitdestroy = False
													besthitdist = dist
													besthitpos = (xwall, ywall)
													besthitvec = (-v[0], -v[1])
												else:
													besthitdestroy = False
													besthitdist = dist
													besthitpos = (xwall, ywall)
													besthitvec = (v[0], -v[1])
											else:
												if neighy:
													besthitdestroy = False
													besthitdist = dist
													besthitpos = (xwall, ywall)
													besthitvec = (-v[0], v[1])
												else:
													besthitdestroy = True
													besthitdist = dist
													besthitpos = (xwall, ywall)
									else:
										# hits the wall, reflect
										besthitdist = dist
										besthitpos = (xwall, ywall)
										besthitvec = (v[0], -v[1])
										besthitdestroy = False
							

			# see if vector will hit myself within the distance allotted
			phome = norm( ( myx - px, myy - py ) )
			#print "p = (%f, %f), my = (%f, %f), phome = %s, v = %s" % (px, py, myx, myy, str(phome), str(v))
#			xp = -1
#			yp = -1
#			if v[1] != 0:
#				s = (myy - py) / v[1]
#				if s > 0:
#					xp = px + s * v[0]
#			else:
#				s = (myx - px) / v[0]
#				if s > 0:
#					yp = py + s * v[1]
				
#			if abs(xp - myx) <= TOL or abs(yp - myy) <= TOL:
			if appeq(phome, v):
				# check length and abort anyway
				dist = vlen( (myx-px, myy-py) )
				#raypath += "\n%f\t%f" % (myx, myy)
				#print "HOME @%f (max %f)!" % (dist, l)
				if (dist <= l) and (dist < besthitdist):
					#print "COUNT %s\n%s\n%f" % (str(vect), raypath.replace('.', ','), l - dist)					
					cnt += 1
				break
			
			if besthitpos == None:
				l = -1.0
			else:
				l -= besthitdist
				px = besthitpos[0]
				py = besthitpos[1]
				v = besthitvec
			#raypath += "\n%f\t%f" % (px, py)
			#print "=> restl = %f, p = (%f, %f), v = %s" % (l, px, py, str(v))
			
			if besthitdestroy:
				# print raypath + " was DESTROYED!"
				l = -1.0
									
	out(cnt)

# ------------------------------------
# GCJ2012 framework stuff
# ------------------------------------
import sys
import os

case_number = 1
lines = []

def out(*vals):
	global case_number
	print "Case #%d:" % case_number,
	for v in vals:
		print str(v),
	print
	case_number += 1
		
def output(fmt, *vals):
	global case_number
	print ("Case #%d: " + fmt) % ((case_number,) + vals)
	case_number += 1

def pop():
	global lines
	e = lines[0]
	lines = lines[1:]
	return e
	
def popint():
	return int(pop())
	
def popflt():
	return float(pop())
	
def main():
	global lines
	case_count = int(pop())
	for x in range(case_count):
		process()
	if len(lines) != 0:
		print "ERROR: %d lines remaining" % (len(lines))

if __name__ == "__main__":
	f = open(sys.argv[1])
	lines = map(lambda x: x[:-1], f.readlines())
	f.close()
	main()
