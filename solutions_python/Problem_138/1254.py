def quicksort(lst):
  n = len(lst)

  if (n <= 1):
    return lst
  else:
    pivot = lst[0]
    less = []
    greater = []

    for i in lst[1:]:
      if (i >= pivot):
        greater.append(i)
      else:
        less.append(i)
    
    return quicksort(less) + [pivot] + quicksort(greater)

def indexOfGreater(lst, n):
    for x, y in enumerate(lst):
        if y > n:
            return x

    return -1

def war(naimo, ken, N):
    naimoPoints = 0

    for block in naimo:
        i = indexOfGreater(ken, block)

        if i == -1:
            naimoPoints += 1

        ken[i] = 0.0


    return naimoPoints

def beatable(naimo, ken, N):
    for i in range(N):
        if naimo[i] < ken[i]:
            return False

    return True

def deceitfulWar(naimo, ken, N):
    n = naimo[:]
    k = ken[:]

    while (N > 0) and (n[0] < k[-1]):
        if beatable(n, k, N):
            return N
        else:
            del n[0]
            del k[-1]

            N -= 1

    return N

f = open('D-large.in', 'r')
o = open('D-large.out', 'w')

T = int(f.readline())

for t in range(T):
    N = int(f.readline())
    naimo = map(float, f.readline().replace('\n', '').split(' '))
    ken = map(float, f.readline().replace('\n', '').split(' '))

    naimo = quicksort(naimo)
    ken = quicksort(ken)

    pointsDW = deceitfulWar(naimo, ken, N)
    pointsW = war(naimo, ken, N)
    
    o.write('Case #%d: %d %d\n' % (t+1, pointsDW, pointsW))
