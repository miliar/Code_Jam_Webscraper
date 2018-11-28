# Maximum difference
def maxdiff(array):
  m = 0

  for i in range(0, len(array) - 1):
    if array[i] - array[i + 1] > m:
      m = abs(array[i] - array[i + 1])

  return m

# Calculations
def mushrooms(length, array):
  # Before
  m = maxdiff(array)

  a = 0
  b = 0

  # First
  for i in range(0, length - 1):
    if array[i] - array[i + 1] >= 0:
      a += array[i] - array[i + 1]

  # Second
  for i in range(0, length - 1):
    if m > array[i]:
      b += array[i]
    else:
      b += m

  # Result
  return [str(a), str(b)]

# Input & Result
for case in range(0, int(input())):
  length = int(input()); array = list(map(int, input().split()))
  print( "Case #%d: %s" % (case + 1, " ".join(mushrooms(length, array))) )