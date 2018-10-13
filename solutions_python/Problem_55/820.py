#*-* coding: utf-8 *-*
from collections import deque

class RollerCoaster(object):
  
  def __init__(self, file):
    self.mode = 'small' if 'small' in file else 'large'
    self.input = open(file, 'r')
    self.testcases = int(self.input.readline().strip())
    self.output = open('/home/ezequiel/output_%s_%s' %(self.__class__.__name__, self.mode), 'w')

  def main(self):
    for i in range(self.testcases):
     
      self.output.write("Case #%s: " %(i+1))
      linea1 = self.input.readline().strip('\n')
      linea2 = self.input.readline().strip('\n')
      
      R, k, N = [int(x) for x in linea1.split()]
      cola = deque([int(x) for x in linea2.split()])
      suma = 0 
      
      for j in range(R):
        subidos = 0
        contador = 0
        while True:
          nuevo = cola.popleft()
          contador += 1
          if subidos + nuevo > k:
            cola.appendleft(nuevo)
            break
          else:
            subidos += nuevo
            cola.append(nuevo)
            if contador == N:
              break
        suma += subidos
      self.output.write(str(suma) + "\n")     

  
s = RollerCoaster('/home/ezequiel/C-small-attempt0.in')
s.main()
