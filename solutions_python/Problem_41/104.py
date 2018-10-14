def next_number(l): # l must NOT be reverse sorted
  if len(l) == 1:
    return l
  
  head, tail = l[0], l[1:]
  sorted_tail = sorted(tail, reverse = True)
  if sorted_tail == tail:
    for i in reversed(sorted_tail):
      if i > head:
        tail.remove(i)
        return [i] + sorted(tail + [head])
  
  return [head] + next_number(tail)

def next(s):
  l = ['0'] + [c for c in s]
  return str(int(''.join(next_number(l))))

if __name__ == "__main__":
  count = int(raw_input())
  for i in range(count):
    s = raw_input()
    print 'Case #' + str(i+1)  + ': ' + next(s)
