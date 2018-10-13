T = int(raw_input())

for c in range(1, T+1):
  line = raw_input().split()
  actions = []
  for i in range(1, len(line), 2):
    actions.append((line[i] == 'O', int(line[i+1])))
  pos_t, pos_f = 1, 1
  btn_t = map(lambda x : x[1], filter(lambda x : x[0], actions))
  btn_f = map(lambda x : x[1], filter(lambda x : not x[0], actions))
  iter = 0
  
  for act_type, act_pos in actions:
    iter_n = abs(act_pos-(pos_t if act_type else pos_f))+1
    iter += iter_n
    if act_type:
      pos_t = btn_t.pop(0)
      assert pos_t == act_pos
      if btn_f:
        pos_f = max(pos_f - iter_n, btn_f[0]) if btn_f[0] < pos_f else min(pos_f + iter_n, btn_f[0])
    else:
      pos_f = btn_f.pop(0)
      assert pos_f == act_pos
      if btn_t:
        pos_t = max(pos_t - iter_n, btn_t[0]) if btn_t[0] < pos_t else min(pos_t + iter_n, btn_t[0])
  
  print 'Case #%d: %d' % (c, iter)

