import os

class Snapper:
	__snap_input__ = None
	__state__ = 0
	__power__ = 0

	def snap(self):
		
		if self.__power__==1:
			if self.__state__==0:
				self.__state__=1
			else:
				self.__state__=0
				
		if self.__snap_input__ is None or self.__snap_input__.__state__==1 and self.__snap_input__.__power__==1:
			self.__power__ = 1
		else:
			self.__power__ = 0
		
		#debug
		#print 'power %d state %d' % (self.__power__,self.__state__)
		
def init_snapper(count):

	snappers = []
	before = None
	actual = None

	# linked list
	for i in xrange(0, count):
		actual = Snapper()
		actual.__snap_input__ = before
		snappers.append( actual )
		before = actual
		
	return snappers

def snap(case, snappers,count):
	
	if count==0:
		return 'Case #%d: OFF\n' % case
	else:
	
		# power on first
		snappers[0].__power__=1
		
		# snapping
		for i in xrange(0, count):
			for snapper in snappers:
				snapper.snap()
			
		ret='OFF'
		if snapper.__power__==1 and snapper.__state__==1:
			ret='ON'
			
		return 'Case #%d: %s\n' % (case, ret)
	
f = open('A-small-attempt0.in','r')
w = open('A-small.out','w')
i=0

for line in f.xreadlines():
	if i>0:
		n,k = line.split()
		snappers = init_snapper(int(n))
		result = snap(i, snappers, int(k))
		w.write(result)
	i=i+1
	

f.close()
w.close()