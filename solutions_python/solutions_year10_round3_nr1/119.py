if __name__ == "__main__" :
		t = int(raw_input())
		for i in xrange(0,t) :
			intersects = 0
			n = int(raw_input())
			a = list()
			for j in xrange(0,n) :
				val = raw_input()
				int_val = map(int,val.split())
				a.append(int_val)
			for items in a :
				indx = a.index(items)
				if indx == 0 :
					pass
				else :
					for range_par in xrange(0,indx) :
						if a[range_par][0] > items[0] :
							if a[range_par][1] < items[1] :
								intersects = intersects + 1
						else :
							if a[range_par][1] > items[1] :
								intersects = intersects + 1
			print "Case #%d: %d" %(i+1,intersects)


