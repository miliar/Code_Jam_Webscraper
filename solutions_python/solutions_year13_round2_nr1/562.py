def solveMote(current_size, levels):
   return _solveMote(current_size, sorted(levels), 0, len(levels))

def _solveMote(current_size, levels, total_operations, initial_size):
   # print 'solveMote(%r, %r, %r)' % (current_size, levels, total_operations)
   if total_operations > initial_size:
      return initial_size

   for level in levels[:]:
      if level < current_size:
         current_size += level
         levels.remove(level)
      else:
         break

   if not levels:
      return total_operations

   # We have levels left, and we're stuck. Branch?
   levels_copy = levels[:]
   del levels_copy[0]

   return min(
      _solveMote(current_size, [current_size - 1] + levels, total_operations + 1, initial_size),
      _solveMote(current_size, levels_copy, total_operations + 1, initial_size)
   )

number_of_test_cases = int(raw_input())
for test_i in range(1, number_of_test_cases + 1):
   (initial_size, _) = map(int, raw_input().split())
   levels = map(int, raw_input().split())
   print "Case #%s: %s" % (test_i, solveMote(initial_size, levels))

# assert 0 == solveMote(2, [2, 1])
# assert 1 == solveMote(2, [2, 1, 1, 6])
# assert 2 == solveMote(10, [9, 20, 25, 100])
# assert 4 == solveMote(1, [1, 1, 1, 1])