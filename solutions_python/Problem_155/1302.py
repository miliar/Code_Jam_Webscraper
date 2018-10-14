import sys

if __name__ == '__main__':
	with open(sys.argv[1]) as f:
		content = f.readlines()
		if len(content)>0:
			t = int(content[0].split('\n')[0])
			
			
			def getAdditionalFriends(s, a):
				if (s==0):
					return 0
					
				else:
					f = 0
					standing = int(a[0])
					#print "S=0 Standing: %s" % standing
					for i in range(1, s+1):
						if standing < i and int(a[i]) > 0:
							lack = i - standing
							f += lack
							standing = i + int(a[i])
							#print "S=%s AddFriends: %s Standing: %s TotalStanding: %s" % (i, lack, a[i], standing)
						else:
							standing += int(a[i])
							#print "S=%s Standing: %s TotalStanding: %s" % (i, a[i], standing)
					
					return f
			
			
			for i in range(1, t+1):
				case = content[i].split('\n')[0].split(' ')
				s_max = int(case[0])
				audience = case[1]
				
				print "Case #%s: %s" % (i, getAdditionalFriends(s_max, audience))
