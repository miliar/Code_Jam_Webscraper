
import copy


class Chest:
	def __init__(self, i, t, keys):
		self.i = i
		self.t = t
		self.keys = keys
		self.visited = False
	
	def add_keys(self, keys):
		for i in self.keys:
			keys[i] += 1
	
	def remove_keys(self, keys):
		for i in self.keys:
			keys[i] -= 1
	
	def __repr__(self):
		return str(self)
	
	def __str__(self):
		return "Chest(%s, %s, %s, %s)" % (self.i, self.t, self.keys, self.visited)
	
	def add_may(self, may):
		for k in self.keys:
			may[k] += 1
	
	def remove_may(self, may):
		for k in self.keys:
			may[k] -= 1
		



def ff(chests, keys, need, may):
	
	for i,n in enumerate(need):
		if may[i] + keys[i] < need[i]:
			#print "Cut", need, may, keys
			return None
	
	for c in chests:
		if not c.visited:
			break
	else:
		return []
	
	for c in chests:
		if not c.visited and not keys[c.t]:
			for cc in chests:
				if cc != c and c.t in cc.keys:
					break
			else:
				#print "Cut2", chests, keys
				return None
	
	
	#print chests
	for c in chests:
		if not c.visited:
			if keys[c.t]:
				keys[c.t] -= 1
				need[c.t] -= 1
				c.remove_may(may)
				c.add_keys(keys)
				c.visited = True
				#print "visit", c, need, may
				r = ff(chests, keys, need, may)
				c.visited = False
				c.remove_keys(keys)
				c.add_may(may)
				need[c.t] += 1
				keys[c.t] += 1
				#print "unvisit", c, need, may
				if isinstance(r, list):
					return [c.i] + r
	
	return None


runs = input()
for run in xrange(runs):
	K,N = [ int(x) for x in raw_input().split() ]
	_keys = [ int(x) for x in raw_input().split() ]
	NK = 40
	keys = [0] * NK
	may = [0] * NK
	need = [0] * NK
	for key in _keys:
		keys[key] += 1
	#print "keys :", keys
	chests = []
	for i in xrange(N):
		l = [ int(x) for x in raw_input().split() ]
		chests.append(Chest(i+1, l[0], l[2:]))
		for k in l[2:]:
			may[k] += 1
		need[l[0]] += 1
	#print keys; print chests, len(chests); print need, may
	r = ff(chests, keys, need, may)
	print "Case #%d:" % (run+1),
	if r:
		print " ".join(( str(x) for x in r ))
	else:
		print "IMPOSSIBLE"
