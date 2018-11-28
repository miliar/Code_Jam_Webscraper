import sys

t = int(sys.stdin.readline())
fc = 0
seconds = 0.0
runAgain = True
prevSeconds = 0.0
op = ''

for tc in range(0,t):
  temp = sys.stdin.readline()
  a = temp.split(' ')
  a[-1] = a[-1].strip()  
  c = float(a[0])
  f = float(a[1])
  x = float(a[2])

  runAgain = True
  fc = 0
  prevSeconds = 0
  seconds = 0
  
  if(c>x):
    seconds = x/2
    op = op + "Case #"+str(tc+1)+": " + str(seconds) + "\n"
  else:
    while runAgain == True:
      
      if(fc == 0):
        seconds = x/2
        prevSeconds = seconds
      elif(fc == 1):
        seconds = 0
        seconds = (c/2) + (x / (2 + (fc * f)))
        if(prevSeconds > seconds):
          prevSeconds = seconds
      else:
        seconds = 0
        for i in range(0,fc):
          seconds += (c/(2+(i*f)))
        else:
          seconds = seconds + (x / (2 + (fc * f)))
          if(prevSeconds > seconds):
            prevSeconds = seconds
          else:
            pass
            
      fc = fc + 1

      if(prevSeconds < seconds):
        op = op + "Case #"+str(tc+1)+": " + str(prevSeconds) + "\n"
        runAgain = False

    else:
      pass
else:
  print(op.strip())
  
