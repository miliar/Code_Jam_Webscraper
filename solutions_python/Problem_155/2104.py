import re
import string
import sys



def return_number(imput):
  aux = imput.split(' ')
  s_max = string.atoi(aux[0])
  s = list(aux[1])
  nb_up = 0
  nb_to_add = 0

  for i in range(0, s_max + 1):
    I = string.atoi(s[i])
    nb_up += I

    if i >= nb_up:
      nb_to_add += 1
      nb_up += 1

  return nb_to_add

def parsing(imput, output):
  m_file = open(imput, "r")
  f = m_file.read()
  lignes = f.split("\n")
  file_output = open(output, "w")


  nb_i = string.atoi(lignes[0])

  for i in range(1, nb_i+ 1):
    print(lignes[i])
    result = return_number(lignes[i])
    file_output.write("Case #"+str(i)+": " + str(result)+ "\n")
  


  m_file.close()
  file_output.close()



  print("end")

parsing("bite.in", "standing_ovation.out")
