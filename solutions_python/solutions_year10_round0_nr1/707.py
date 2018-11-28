#!/usr/bin/python2.4 -tt
# -*- coding: utf-8 -*-


def main():
  num_cases = input();
  for i in range(num_cases):
    NK = raw_input().split(' ');
    N = int(NK[0]);
    K = int(NK[1]);

    KN = 0;
    if(K != 0):
      if(K > N):
	KN = K%(2**N);
      else:
	KN = K;
    
    
    if(K != 0 and KN == (2**N) - 1):
      print 'Case #'+str(i+1)+': ON';
    else:
      print 'Case #'+str(i+1)+': OFF';



if __name__ == '__main__':
  main()