f = open('A-small-attempt3.in', 'r')

ulang = raw_input()
ulang = int(ulang)
jumlah = range(ulang)

baris1 = []
baris2 = []
result = []

def comparelist(list1, list2):
  list1 = list1.split()
  list2 = list2.split()
  count = 0
  value = 0
  for val in list1:
    if val in list2:
      count += 1
      value = val
  if count == 0:
    return 0
  elif count == 1:
    return value
  else:
    return -1

for i in jumlah:
  pilih1 = int(raw_input())
  baris1.append(raw_input())
  baris1.append(raw_input())
  baris1.append(raw_input())
  baris1.append(raw_input())
  pilih2 = int(raw_input())
  baris2.append(raw_input())
  baris2.append(raw_input())
  baris2.append(raw_input())
  baris2.append(raw_input())
  tebak1 = baris1[pilih1 - 1]
  tebak2 = baris2[pilih2 - 1]
  result.append(comparelist(tebak1, tebak2))
  baris1[:] = []
  baris2[:] = []

for i in jumlah:
  urut = i + 1
  if result[i] == 0:
    print "Case #%d: Volunteer cheated!" % urut
  elif result[i] == -1:
    print "Case #%d: Bad magician!" % urut
  else:
    print "Case #%d: %s" % (urut, result[i])