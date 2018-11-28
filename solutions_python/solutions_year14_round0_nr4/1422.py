import sys


def process_case(naomi, ken):
  y = 0
  z = 0

  naomi.sort()
  ken.sort()
  naomi2 = list(naomi)
  ken2 = list(ken) 
  for i in range(0, len(naomi)):
    if ken[len(ken)-1] < naomi[len(naomi)-1]:
      y+=1
      ken.pop()
      naomi.pop()
    else:
      ken.pop()
      naomi = naomi[1:]

  #truthful
  
  for i in range(0, len(naomi2)):
    z+=1
    ken_wins = False
    for x in range(0, len(ken2)):
      if ken2[x] > naomi2[i]:
        del ken2[x]
        z= z-1
        ken_wins = True
        break
    if ken_wins == False:
      ken2 = ken2[1:]
  
        
        

     
  return str(y) + " " + str(z)  

def main():
  testcases =0
  output = []

  with open(sys.argv[1]) as file:

    testcases= int(file.readline())
    for i in range(0, testcases):
      naomi = []
      ken = []
      num_inputs = int(file.readline())
      naomi = [float(x) for x in file.readline().split()]
      ken = [float(x) for x in file.readline().split()]
      output.append(process_case(naomi, ken))

  for i in range(0, len(output)):
    print "Case #"+ str(i+1) +": " +  output[i]



if __name__=='__main__':
  main()
