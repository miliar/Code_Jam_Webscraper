fi=open("input.txt","r")
fo=open("output.txt","w")
T=int(fi.readline().strip())
for j in range(T):
  st=fi.readline().strip()
  ls=st.split()
  r=int(ls[0])*2-1
  t=int(ls[1])
  i=int(((8*t+r**2)**0.5 -r)/4)
  st="Case #"+str(j+1)+": "+str(i) + "\n"
  fo.write(st)
fo.close()
fi.close()

