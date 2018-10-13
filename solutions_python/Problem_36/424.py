def index(array, c):
  result = []
  for i in range(len(array)):
    if(array[i] == c):
      result.append(i)
  return result

def filter_by(array, pos):
  length = len(array)
  for i in range(length):
    if(array[i] > pos):
      return range(i,length)
  return []

def count(test):
  index_w = index(test, 'w')
  index_e = index(test, 'e')
  index_l = index(test, 'l')
  index_c = index(test, 'c')
  index_o = index(test, 'o')
  index_m = index(test, 'm')
  index__ = index(test, ' ')
  index_t = index(test, 't')
  index_d = index(test, 'd')
  index_j = index(test, 'j')
  index_a = index(test, 'a')

  counter = 0
  for b in filter_by(index_w, -1):
    for c in filter_by(index_e, index_w[b]):
      for d in filter_by(index_l, index_e[c]):
        for e in filter_by(index_c, index_l[d]):
          for f in filter_by(index_o, index_c[e]):
            for g in filter_by(index_m, index_o[f]):
              for h in filter_by(index_e, index_m[g]):
               for i in filter_by(index__, index_e[h]):
                 for j in filter_by(index_t, index__[i]):
                   for k in filter_by(index_o, index_t[j]):
                     for l in filter_by(index__, index_o[k]):
                       for m in filter_by(index_c, index__[l]):
                         for n in filter_by(index_o, index_c[m]):
                           for o in filter_by(index_d, index_o[n]):
                             for p in filter_by(index_e, index_d[o]):
                               for q in filter_by(index__, index_e[p]):
                                 for r in filter_by(index_j, index__[q]):
                                   for s in filter_by(index_a, index_j[r]):
                                     counter += len(filter_by(index_m, index_a[s]))
  return counter


f = open('C-small-attempt1.in', 'r')
for ind in range(int(f.readline())):
  line = f.readline()
  print 'Case #%(ind)d: %(cnt)04d' % {'ind': ind + 1, "cnt": count(line)}


