f_in=open("B-large.in","r")
lines = f_in.readlines()
i=0
N=int(lines[i])
for ii in range(N):
      i=i+1
      words=lines[i].split()
      rc=[int(w) for w in words]
      r=rc[0]
      c=rc[1]
      m=[]
      for ir in range(r):
         i=i+1
         m.append( [int(w) for w in lines[i].split()] )
      n_sink=0
      rs=[]
      cs=[]
      conn=[[ [] for x in range(c)] for y in range(r)]
      for ir in range(r):
            for ic in range(c):
                  sink_N=False
                  sink_S=False
                  sink_W=False
                  sink_E=False
                  at_N=10001
                  at_S=10001
                  at_W=10001
                  at_E=10001
                  if ir>0:
                        if m[ir-1][ic]<m[ir][ic]:
                              sink_N=True
                              at_N=m[ir-1][ic]
                  if ir<r-1:
                        if m[ir+1][ic]<m[ir][ic]: 
                              sink_S=True
                              at_S=m[ir+1][ic]
                  if ic>0:
                        if m[ir][ic-1]<m[ir][ic]:
                              sink_W=True
                              at_W=m[ir][ic-1]
                  if ic<c-1:
                        if m[ir][ic+1]<m[ir][ic]: 
                              sink_E=True
                              at_E=m[ir][ic+1]
                  not_sink = sink_N or sink_S or sink_W or sink_E
                  if not_sink == False:
                        n_sink=n_sink+1
                        rs.append(ir)
                        cs.append(ic)
                  else:
                        min_at=min([at_N,at_S,at_W,at_E])
                        if at_N==min_at:
                              conn[ir][ic].append("N")
                              conn[ir-1][ic].append("S")
                        elif at_W==min_at:
                              conn[ir][ic].append("W")
                              conn[ir][ic-1].append("E")
                        elif at_E==min_at:
                              conn[ir][ic].append("E")
                              conn[ir][ic+1].append("W")
                        else:
                              conn[ir][ic].append("S")
                              conn[ir+1][ic].append("N")
      bas_kind = "abcdefghijklmnopqrstuvwxyz"
      rest = [ [x,y] for x in range(c) for y in range(r)]
      f_rest = [[ True for x in range(c)] for y in range(r)]      
      basin = [[ [] for x in range(c)] for y in range(r)]
      ibas = -1
      while len(rest) > 0:
            ibas = ibas + 1
            slist = [rest[0]]
            c_bas = bas_kind[ibas]
            while len(slist) > 0:
                  ic,ir = slist[0]
                  basin[ir][ic] = c_bas
                  del slist[0]
                  f_rest[ir][ic] = False
                  for direct in conn[ir][ic]:
                        if direct == "N" and basin[ir-1][ic] == []:
                              basin[ir-1][ic] = c_bas
                              slist.append([ic,ir-1])
                        elif direct == "W" and basin[ir][ic-1] == []:
                              basin[ir][ic-1] = c_bas
                              slist.append([ic-1,ir])
                        elif direct == "E" and basin[ir][ic+1] == []:
                              basin[ir][ic+1] = c_bas
                              slist.append([ic+1,ir])
                        elif direct == "S" and basin[ir+1][ic] == []:
                              basin[ir+1][ic] = c_bas
                              slist.append([ic,ir+1])
            rest=[]
            for ir in range(r):
                  for ic in range(c):
                        if f_rest[ir][ic]==True:
                              rest.append([ic,ir])
      out = "Case #"+str(ii+1)+":"
      print out
      for ir in range(r):
            for ic in range(c):
                  print basin[ir][ic],
            print " "
f_in.close()
