#!/usr/bin/env python

filename = 'large_bot.txt'

def main():
  f = open(filename)  
  testcase_num = int(f.readline())
  for i in xrange(testcase_num):
    line = f.readline().strip().split()
    buttons_num = int(line[0])
    buttons_seq = []
    blue_seq = []
    orange_seq = []
    for j in xrange(buttons_num):
      buttons_seq.append((line[j * 2 + 1], int(line[j * 2 + 2])))
      if line[j * 2 + 1] == 'B':
        blue_seq.append(int(line[j * 2 + 2]))
      else:
        orange_seq.append(int(line[j * 2 + 2]))
    # print buttons_seq
    # print blue_seq
    # print orange_seq

    blue_status = 1
    orange_status = 1
    move = 0
    while len(buttons_seq) > 0:
      # print 'Blue: ' + str(blue_status) + ', Orange: ' + str(orange_status)
      move += 1
      if buttons_seq[0][0] == 'B':
        if blue_status == blue_seq[0]:
          buttons_seq = buttons_seq[1:] # the Blue click the button
          blue_seq = blue_seq[1:]
          # print 'Blue click the button'
        elif blue_status < blue_seq[0]:
          blue_status += 1 # the Blue move toward the button
        else:
          blue_status -= 1 # the Blue move toward the button
        if len(orange_seq) > 0:
          if orange_status > orange_seq[0]:
            orange_status -= 1 # the Orange move toward the button
          elif orange_status < orange_seq[0]:
            orange_status += 1
      else:
        if orange_status == orange_seq[0]:
          buttons_seq = buttons_seq[1:] # the Orange click the button
          orange_seq = orange_seq[1:]
          # print 'Orange click the button'
        elif orange_status < orange_seq[0]:
          orange_status += 1 # the Orange move toward the button
        else:
          orange_status -= 1 # the Orange move toward the button
        if len(blue_seq) > 0:
          if blue_status > blue_seq[0]:
            blue_status -= 1 # the Blue move toward the button
          elif blue_status < blue_seq[0]:
            blue_status += 1 # the Blue move towrad the button
    print 'Case #' + str(i+1) + ': ' + str(move)

if __name__ == '__main__':
  main()
