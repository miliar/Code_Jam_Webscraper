def A(filename):
         fob = open(filename,'r')
         out = open('/home/hussein/a.out','w')
         for tc in xrange(1,int(fob.next().rstrip('\r\n'))+1):
		 line1=[]
		 line2=[]
                 vol1=int(fob.next().rstrip('\r\n'))
                 for i in range(1,5):
                         line=fob.next().rstrip('\r\n').split()
                         if i==vol1:
				 line1=line
                 vol2 = int(fob.next().rstrip('\r\n'))
                 for i in range(4):
                         line = fob.next().rstrip('\r\n').split()
                         if vol2 == (i+1):
                                 line2=line
		 inter =[x for x in line1 if x in line2]
		 if len(inter) ==0:
			 case = 'Volunteer cheated!'
		 elif len(inter) ==1:
			 case = inter[0]
		 else:
			 case = 'Bad magician!'
		 out.write('Case #%d: %s\n' % (tc,case))

         fob.close()
         out.close()
                                
