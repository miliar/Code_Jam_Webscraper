#! /usr/bin/python2

def sean_sum(pile):
  # add all items in set
  real_sum = 0
  for sweet in pile:
    real_sum += sweet
  return real_sum

def patrick_sum(pile):
  # make xor of all items in set
  patrick_sum = 0
  for sweet in pile:
    patrick_sum ^= sweet
  return patrick_sum

# problem is easy once understood:
# if all items xor to zero then sean can make it - just take the
# smallest item for patrick, all the others for him
# if all items do not xor to zero then sean cannot make it

def main():
  # read in number of test cases
  ntc = int(raw_input())
  for i in range(ntc):
    n_candy = int(raw_input())
    words = raw_input().split(None)
    candies = []
    for j in range(n_candy):
      candies.append(int(words[j]))
    if patrick_sum(candies) != 0:
      print "Case #{0}: NO".format(i+1)
    else:
      print "Case #{0}: {1}".format(i+1, sean_sum(candies)-min(candies))

if __name__ == '__main__':
  main()
