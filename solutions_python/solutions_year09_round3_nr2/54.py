#!/usr/bin/env python

import sys;
import string;
import math;


class firefly:
	def __init__(self,init=[0,0,0,0,0,0]):
		( self.x, self.y, self.z, self.vx, self.vy, self.vz ) = init;
	def nextpos(self):
		x = self.x + self.vx;
		y = self.y + self.vy;
		z = self.z + self.vz;
		return [x,y,z];
	def pos(self):
		return [self.x,self.y,self.z];


class point:
	def __init__(self,init=[0,0,0]):
		(self.x,self.y,self.z) = init;
	def printout(self):
		print "x: %f y: %f z: %f" % (self.x,self.y,self.z);
	def tolist(self):
		return [self.x,self.y,self.z];


def centerofmass_now(ffs):
	xc=0;
	yc=0;
	zc=0;
	for ff in ffs:
		p = point(ff.pos());
		xc+=p.x;
		yc+=p.y;
		zc+=p.z;

	xc = float(xc) / len(ffs);
	yc = float(yc) / len(ffs);
	zc = float(zc) / len(ffs);
	return point([xc,yc,zc])


def vel_of_centerofmass(ffs):		
	vxc=0;
	vyc=0;
	vzc=0;

	xc=0;
	yc=0;
	zc=0;

	for ff in ffs:
		p = point(ff.nextpos());
		xc += p.x;
		yc += p.y;
		zc += p.z;

	xc = float(xc) / len(ffs);
	yc = float(yc) / len(ffs);
	zc = float(zc) / len(ffs);

	p = centerofmass_now(ffs);
	return point( map(lambda x,y:x-y,[xc,yc,zc], p.tolist() ) );
					





N = int(sys.stdin.readline());

for i in xrange(N):
        number = int(sys.stdin.readline());
	ff = [];
	for v in xrange(number):
		ff.append( firefly( [ int(x) for x in sys.stdin.readline().split() ] ) );

	com = centerofmass_now(ff);
	v_com = vel_of_centerofmass(ff);

	if v_com.x == 0 and v_com.y == 0 and v_com.z == 0:
		t_min = 0;
	else:	
		t_min = -float(v_com.x*com.x + v_com.y*com.y + v_com.z*com.z) / (v_com.x**2 + v_com.y**2 + v_com.z**2);
		if t_min < 0:
			t_min=0;
	pos_min = point([com.x + v_com.x*t_min, com.y + v_com.y*t_min, com.z + v_com.z*t_min ]);
	d_min = math.sqrt( reduce(lambda x,y:x+y, map(lambda x:x**2,pos_min.tolist() ) ) );
	print "Case #%d: %.8f %.8f" % (i+1,d_min,math.fabs(t_min))
	
