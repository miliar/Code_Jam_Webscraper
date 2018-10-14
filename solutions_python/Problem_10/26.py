#! /usr/bin/python

fd = open("input.in")

num_cases = int(fd.readline())

for i in range(0, num_cases):
  (P, K, L) = [int(item) for item in fd.readline().split(" ")]
  letters = [int(item) for item in fd.readline().split(" ")]

  letters.sort()
  letters.reverse()

  step = 0
  num_presses = 0
  for j in range(0, len(letters)):
    if (j % K) == 0:
      step += 1
    num_presses += letters[j] * step
    if step > P:
      num_presses = "Impossible"
      break

  print "Case #%d:" % (i+1), num_presses
