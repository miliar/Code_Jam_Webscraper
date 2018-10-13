

def main():
   f=open("A-small-attempt0.in",'r')
   wr=open("out.txt",'w')

   t=int(f.readline())

   for ii in range(t):

      a=f.readline()
      a=a.split()
      smax=int(a[0])
      st=list(a[1])
      ct=0
      ans=int(st[0])
      for i in range(smax):

         if(ans>=(i+1)):
            ans=ans+int(st[i+1])
         else:
            ct=ct+(i+1-ans)
            ans=ans+ct
      ot="Case #"
      ot+=str(ii+1)
      ot+=": "
      ot+=str(ct)
      ot+='\n'
      wr.write(ot)


main()