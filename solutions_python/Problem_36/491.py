
f = open('/home/norman/Desktop/untitled folder/input', 'r')
h = open('/home/norman/Desktop/untitled folder/output', 'w')

number_inputs = int(f.readline())
for gg in range(number_inputs):



  string = f.readline() #"aabacbca" #"aabaaadsfbsnfbjksfdcsa,nbds,a,anbsdc,bnad,cba,bcabcbascbndsabc,abc"
  series = "welcome to code jam"#"abc"
  answer_1 = []
  answer_2 = []

  for ii in range(0, len(string)):
    answer_1.append(0)
    answer_2.append(0)


  for ii in range(len(string) , 0, -1):
    if ii == len(string):
      if string[len(string)-1] == series[len(series)-1]:
        answer_1[ii-1] = 1
      else: answer_1[ii-1] = 0
    else:
      if string[ii-1] == series[len(series)-1]:
        answer_1[ii-1] = answer_1[ii] + 1
      else:
        answer_1[ii-1] = answer_1[ii]

  for jj in range(2, len(series)+1):
    for ii in range(len(string) , 0, -1):
      if ii == len(string):
        if string[len(string)-1] == series[len(series)-jj]:
          answer_2[ii-1] = 0
        else: answer_2[ii-1] = 0
      else:
        if string[ii-1] == series[len(series)-jj]:
          answer_2[ii-1] = answer_2[ii] + answer_1[ii-1]
        else:
          answer_2[ii-1] = answer_2[ii]
    answer_1 = answer_2

  answer = answer_1[0]
  answer = str(answer%10000)

  if len(answer) == 4:
    final_answer = "Case #" + str(gg+1) + ": " + answer + "\n"
  if len(answer) == 3:
    final_answer = "Case #" + str(gg+1) + ": " + "0" + answer + "\n"
  if len(answer) == 2:
    final_answer = "Case #" + str(gg+1) + ": " + "00" + answer + "\n"
  if len(answer) == 1:
    final_answer = "Case #" + str(gg+1) + ": " + "000" + answer + "\n"

  print final_answer
  h.write (final_answer)

