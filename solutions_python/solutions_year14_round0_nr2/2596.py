#!/usr/bin/env python3
# coding: utf-8
import sys

def solve(C,F,X):
  rate = 2
  time = C / rate
  while True:
    # temps qu'il reste
    eta = (X-C) / rate
    # temps qu'on aurait en rachetant une usine
    etb = X / (rate + F)
    if eta < etb:
      # on n'aura pas notre objectif plus tôt
      return time + eta
    else:
      # on rachète une usine
      rate += F
      # on retourne au moment où on se pose des questions
      time += C / rate

if __name__ == '__main__':
  cases = [[float(i) for i in z.split()] for z in sys.stdin.read().splitlines()[1:]]
  for i in range(len(cases)):
    print('Case #{}: {:.07f}'.format(i+1,solve(*cases[i])))
