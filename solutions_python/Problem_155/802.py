import sys
zc=ord('0')
if __name__ == '__main__':
	n = int(sys.stdin.readline())
	i=1
	while i <= n:
		for line in sys.stdin:
			ans=0
			q=line.split()[1]
			index=0
			s=0
			for a in q:
				curr=ord(a)-zc
				if curr>0:
					if s<index:
						ad=index-s
						ans+=ad
						s+=ad
					s+=curr
				index+=1
			print 'Case #%d: %d' % (i, ans)
			i+=1
