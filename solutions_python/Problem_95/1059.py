d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q', 'q': 'z'}

count = int(raw_input())
for cases in range(1, count+1):
   raw_msg = raw_input()
   decoded_msg = []
   for ch in range(0, len(raw_msg)):
      decoded_msg.append(d[raw_msg[ch]])
   print "Case #%d: %s" % (cases, "".join(decoded_msg))
