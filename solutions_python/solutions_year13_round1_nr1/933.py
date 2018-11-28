def A(filename):
         fob = open(filename,'r')
         out = open('/home/hussein/Programming/a.out','w')
         for tc in xrange(1,int(fob.next().rstrip('\r\n'))+1):
                  

                  out.write('Case #%d: %s\n' % (tc,case))
         fob.close()
         out.close()
