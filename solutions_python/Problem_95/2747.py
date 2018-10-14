str1 = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvzq"

str2 = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupqz"

dict = {}
length = len(str1)
i=0
while i<length:
    dict[str1[i]] = str2[i]
    i+=1
    
    
n = raw_input()
n = int(n)
i = 0
while i<n:
      line = raw_input()
      output = []
      for ch in line:
	  if ch != ' ':
	     output.append(dict[ch])
	     
	  else:
	     output.append(ch)
      output = ''.join(output)
      string = "Case #" + str(i+1) + ": " + output
      print string
      i+=1