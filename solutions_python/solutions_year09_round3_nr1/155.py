def baseNto10(ln,base):
  if base==0:
   base=2
  ln.reverse()
  c=0
  sum=0
  for a in ln:
    sum+=a*base**c
    c+=1
  return sum




if __name__ == '__main__':     cases = int(raw_input())
     for case in xrange(cases):

          num = raw_input()
          md={}
          res=[]
          last=1
          for a in num:
             if a in md.keys():
                res.append(md[a])
             else:
                md[a]=last
                res.append(last)
                if last==0: 
                   last=2
                elif last==1:
                   last=0
                else:
                   last+=1
          print 'Case #%d:' % (case+1), baseNto10(res,last)    
