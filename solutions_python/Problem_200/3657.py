def goodq(s):
  observed_max = s[0]
  for digit in s:
    if int(digit) > int(observed_max):
      observed_max = digit
    if int(digit) < int(observed_max):
      return False
  return True

def goodq_test_case(s, t):
  assert goodq(s) == t

# goodq_test_case("4", True)
# goodq_test_case("123", True)
# goodq_test_case("224488", True)
# goodq_test_case("132", False)
# goodq_test_case("1000", False)
# goodq_test_case("11110", False)

def descend_naive(s):
  x = int(s)
  while x >= 0:
    s = str(x)
    if goodq(s):
      return s
    x -= 1
  assert False

# assert descend_naive("132") == "129"
# assert descend_naive("1000") == "999"
# assert descend_naive("7") == "7"
# assert descend_naive("111111111111111110") == "99999999999999999"
# assert descend_naive("13332") == "12999"

def descend_1_round(s):
  # Run through the numbers RTL
  # If a pair (x,y) is such that x > y (descends)
  # Then set x to x-1 and the rest to 9s.
  # Worry about x == 0, but maybe that's impossible.
  for i in xrange(len(s)-1, 0, -1):
    x, y = int(s[i-1]), int(s[i])
    # print "pair", s[0:i-1] + "[" + s[i-1:i+1] + "]" + s[i+1:]
    if x > y:
      raw = s[0:i-1] + str(x-1) + ("9" * (len(s)-i))
      # print "into", s[0:i-1] + "[" + str(x-1) + ("9" * (len(s)-i)) + "]"
      return str(int(raw))
  return s

# assert descend_1_round("5") == "5"
# assert descend_1_round("15") == "15"
# assert descend_1_round("51") == "49"
# assert descend_1_round("132") == "129"
# assert descend_1_round("13329") == "13299"

def descend(s):
  s1 = s
  # limited fixed point loop
  for _ in xrange(len(s) + 2):
    # print "s1", s1
    s2 = descend_1_round(s1)
    # print "s2", s2
    if s1 == s2:
      assert goodq(s2)
      return s2
    s1 = s2
  assert False

# assert descend("7") == "7"
# assert descend("78") == "78"
# assert descend("84") == "79"
# assert descend("132") == "129"
# assert descend("1000") == "999"
# assert descend("111111111111111110") == "99999999999999999"
# assert descend("13332") == "12999"
# assert descend("394036361354610669") == "389999999999999999"

# 1110
# 1109
# 1099
# 0999

# 132
# 129

# 13332
# 13329
# 13299
# 12999

if __name__ == "__main__":
  ncases = int(raw_input())
  for i in xrange(ncases):
    x = int(raw_input())
    y = descend(str(x))
    print "Case #{}: {}".format(i+1, y)
