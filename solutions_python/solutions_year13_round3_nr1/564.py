def roundC_A(filename):
         fob = open(filename,'r')
         out = open('/home/hussein/Programming/a.out','w')
         for tc in xrange(1,int(fob.next().rstrip('\r\n'))+1):
                  s = fob.next().rstrip('\r\n').split(' ')
                  count=0
                  name = s[0]
                  n = int(s[1])
                  s_len = len(name)
                  vouwels=['a','u','o','i','e']
                  for i in range(s_len):
                           for j in range(s_len):
                                    s = name[i:j+1]
                                    if s=='':
					    continue
				    temp =0
				    l = list(s)
				    for k in l:
					     if k not in vouwels:
						      temp+=1
						      if temp>=n:
							       count+=1
							       break
					     else:
						      temp=0
						      continue
				    temp=0

                  out.write('Case #%d: %s\n' % (tc,count))
         fob.close()
         out.close()
