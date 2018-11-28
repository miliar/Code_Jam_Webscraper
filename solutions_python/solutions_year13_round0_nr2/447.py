#!/usr/bin/python
import os,io,math,sys

def run(filename):

  fin = open(filename, 'r')
  fout = open('output.out','w')
  T = int(fin.readline())
  for t in range(T):
    # read
    [N,M]=fin.readline().split(" ")
    N = int(N)
    M = int(M)
    ttt = []
    for i in range(N):
      line = fin.readline()
      row = [ int(e) for e in line.split(" ") ]
      ttt.append(row[0:M])
    print "Read done",t
    #print ttt

    # solve
    transttt = zip(*ttt)
    #print transttt

    mat = [[100]*M for x in range(N)]
    for i in range(N):
      m = max(ttt[i])
      mat[i] = [ e if e<m else m for e in mat[i] ]
      #for r in mat:
      #  print r
      #print
    for j in range(M):
      m = max(transttt[j])
      for i in range(N):
        mat[i][j] = mat[i][j] if mat[i][j]<m else m
      #for r in mat:
      #  print r
      #print

    # calcRes
    same = True
    for i in range(N):
      for j in range(M):
        if ttt[i][j] != mat [i][j]:
          same = False
          break
      if not same:
        break

    # write
    fout.write("Case #%d: %s\n" %(t+1,'YES' if same else 'NO') )
 
  fin.close()
  fout.close()

if __name__ == "__main__":
  run(sys.argv[1])
