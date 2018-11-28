class Robot(object):
  def __init__(self, buttons):
    self.location = 0
    self.buttons = buttons

  def is_done(self):
    if self.buttons == []:
      return True
    return False
  def try_push(self, sequence):
    next_location = self.buttons[0][0]
    next_sequence = self.buttons[0][1]
    if self.location != next_location:
      if self.location > next_location:
        self.location -= 1
        return False
      elif self.location < next_location:
        self.location += 1
        return False
    if sequence == next_sequence:
      del self.buttons[0]
      return True
    return False
      
def compute_secs(orange, blue):
  o_robot = Robot(orange[:])
  b_robot = Robot(blue[:])
  secs = 0
  sequence = 0
  while (not o_robot.is_done()) or (not b_robot.is_done()):
    o_ret = False
    b_ret = False
    if not o_robot.is_done():
      o_ret = o_robot.try_push(sequence)
    if not b_robot.is_done():
      b_ret = b_robot.try_push(sequence)

    if o_ret or b_ret:
      sequence += 1
    secs += 1
    
  return secs-1




if __name__ == '__main__':
  num_of_cases = int(raw_input())
  for case_index in range(num_of_cases):
    sequence = raw_input().strip().split()
    num_of_terms = int(sequence[0])
    orange = []
    blue = []
    for i in range(num_of_terms):
      color, button = sequence[1 + 2*i],sequence[2 + 2*i]
      if color == 'O':
        orange.append((int(button),i))
      elif color == 'B':
        blue.append((int(button),i))

    num_of_secs = compute_secs(orange, blue)
    print "Case #%d: %d" % (case_index+1, num_of_secs)
