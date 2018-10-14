def lightIsOn(numSnappers, snaps):
  period = 2 ** numSnappers
  if (snaps % period) is (period - 1):
    return 'ON'
  else:
    return 'OFF'

def main():
  f = open('small2.in', 'r')
  numLines = int(f.readline())
  for i in range(numLines):
    input = f.readline()
    n,k = input.split(' ')
    n = int(n)
    k = int(k)
    print 'Case #' + str(i+1) + ':', lightIsOn(n, k)

main()
