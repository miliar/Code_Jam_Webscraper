if __name__ == "__main__" :
		t = int(raw_input())
		for i in xrange(0,t) :
			inp = raw_input()
			listval = map(int,inp.split())
			l = listval[0]
			p = listval[1]
			c = listval[2]
			inc = 0
			ans = 0
			check = l*c
			while(check < p) :
				check = check * c
				inc = inc + 1
			if inc == 0 or inc == 1 or inc == 2 :
				ans = inc
			else :
				x = inc
				while (x != 1) :
					x = x/2
					ans += 1
				ans += 1

			print "Case #%d: %d" %(i+1,ans)
