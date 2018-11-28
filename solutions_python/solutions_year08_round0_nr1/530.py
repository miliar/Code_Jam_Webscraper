def main():
  for case in range(input()):
    engines = set()
    temp = set()
    k = 0
    n = input()
    for i in range(n):
      engines.add(raw_input())
    for j in range(input()):
      query = raw_input()
      if query not in temp:
        temp.add(query)
        if len(temp) == n:
          k += 1
          temp = set([query])
    print 'Case #%s: %s' % (case + 1, k)
main()