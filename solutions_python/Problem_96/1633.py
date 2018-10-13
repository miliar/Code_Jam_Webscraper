data = [l.strip() for l in open("infile", "r").readlines()]
out = open("outfile", "w")

ncases = int(data.pop(0))
for case in range(ncases):
  casedata = data.pop(0).split(' ')
  ngooglers = int(casedata.pop(0))
  nsurprises = int(casedata.pop(0))
  best = int(casedata.pop(0))
  
  nosurprise = 0
  either = 0
  surprise = 0

  for score in casedata:
    score = int(score)
    withoutsurprise = False
    withsurprise = False
    if score > 3 * (best-1):
      withoutsurprise = True
    if score >= 2 and score <= 28 and score > ((best-1)*3 - 2):
      withsurprise = True
    if withsurprise:
      if withoutsurprise:
        either += 1
      else:
        surprise += 1
    elif withoutsurprise: 
      nosurprise += 1
 
  surprisesused = min(surprise, nsurprises)      
  either -= (nsurprises - surprisesused)
  total = nosurprise + either + nsurprises
        
  out.write("Case #" + str(case + 1) + ": " + str(total) + "\n")

