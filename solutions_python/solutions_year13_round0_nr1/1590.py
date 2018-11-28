#!/usr/bin/python2

class Game:

  # table is a 16-char line holding the state
  def setState(self, table):
    self.state = table

  # Check possible end states. player is either 'X' or 'O'
  def checkDiags(self, player):
    
    #Two possible diagonals

    # Principal
    for i in range(4):
      if self.state[5*i] != player and self.state[5*1] != 'T':
        break
      elif i == 3:
        return True

    # Secondary
    for i in range(4):
      if self.state[3*(i+1)] != player and self.state[3*(i+1)] != 'T':
        break
      elif i == 3:
        return True

    return False
    
  def checkCols(self, player):
    for c in range(4):
      if self.state[c] != player and self.state[c] != 'T':
        continue
      else:
        for l in range(1,4):
          if self.state[c + l*4] != player and self.state[c + l*4] != 'T':
            break
          elif l == 3:
            return True

    return False

  def checkRows(self, player):
    for l in range(4):
      if self.state[4*l] != player and self.state[4*l] != 'T':
        continue
      else:
        for c in range(1,4):
          if self.state[c + l*4] != player and self.state[c + l*4] != 'T':
            break
          elif c == 3:
            return True

    return False
      

if __name__ == "__main__":

  g = Game()

  f = open('sample', 'r')

  # Number of samples
  n = f.readline()

  for i in range(int(n)):

    state = ''
    for j in range(4):
      state += f.readline()

    # Discard empty line after each table
    f.readline()

    # Replace new lines
    state = state.replace('\n', '')

    # Strip new lines
    #g.setState(state.replace('\n',''))
    g.setState(state)

    for player in ['O', 'X']:

      if g.checkDiags(player) == True:
        print "Case #"+str(i+1)+": "+player+" won"
        break

      elif g.checkCols(player) == True:
        print "Case #"+str(i+1)+": "+player+" won"
        break

      elif g.checkRows(player) == True:
        print "Case #"+str(i+1)+": "+player+" won"
        break

      # Quick and dirty: if its the last check
      if player == 'X':
        if state.find('.') == -1:
          print "Case #"+str(i+1)+": Draw"

        else:
          print "Case #"+str(i+1)+": Game has not completed"
