#!/usr/bin/python2.4 -tt
# -*- coding: utf-8 -*-


def main():
  num_cases = input();
  for i in range(num_cases):
    RkN = raw_input().split(' ');
    g = raw_input().split(' ');
    
    gp = 0; Gp = 0; G = [0]; more = 0;
    while (Gp < int(RkN[0])):
      if(gp == int(RkN[2])):
	gp = 0;
	if(more == 0):
	  Gp += 1;
	  G.append(0);
	  more += 1;
	more -= 1;

      if(G[Gp] + int(g[gp]) > int(RkN[1])):
	Gp += 1;
	G.append(0);
	more += 1;
      G[Gp] += int(g[gp]);
      gp += 1;

    print 'Case #'+str(i+1)+':',sum(G[:-1]);




if __name__ == '__main__':
  main()
