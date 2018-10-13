f=open("B-small-attempt0.in","r")
out = open('workfile', 'w')
T=int(f.readline())
for x in range(T):
  row=map(float,str(f.readline()).split())
  rate=2
  seconds=0
  while 1:
    time_until_done=row[2]/rate
    time_until_next_farm=row[0]/rate
    tud_after_next_farm=row[2]/(rate+row[1])
    if time_until_next_farm+tud_after_next_farm>time_until_done:
      seconds+=time_until_done
      out.write("Case #"+str(x+1)+": "+("{0:.7f}".format(seconds))+"\n")
      break
    else:
      seconds+=time_until_next_farm
      rate+=row[1]