def main():
  T = input()
  for t in xrange(T):
    cmds = raw_input().split()[1:]
    opos = 1
    bpos = 1
    olastt = 0
    blastt = 0
    lastt = 0
    for i in xrange(0,len(cmds),2):
      tmp = int(cmds[i+1])
      if cmds[i]=='O':
        olastt = max(abs(tmp - opos) + olastt+1,lastt+1)
        opos = tmp
        lastt = olastt
      else:
        blastt = max(abs(tmp - bpos) + blastt+1, lastt+1)
        bpos = tmp
        lastt = blastt
    print "Case #%d: %d"%(t+1,max(blastt,olastt))

main()
