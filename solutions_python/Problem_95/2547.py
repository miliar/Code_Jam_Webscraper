#!/usr/bin/python2.7 -tt
# coding: utf-8

import sys, string

def ler(ficheiro):
  s = []
  try:
    f = open(ficheiro, 'rU')
    for line in f:
      s.append(line),
    f.close()
  except IOError:
    print 'Ficheiro ' + ficheiro + ' não encontrado!'
  s = map(lambda ss: ss.strip(), s)
  return s

def traduzir(texto):
  linha = int(1)
  f = open('output.txt', 'w')
  for frase in texto:
    frase_traduzida = string.translate(frase, string.maketrans("abcdefghijklmnopqrstuvwxyz", "yhesocvxduiglbkrztnwjpfmaq"))
    f.write('Case #'+str(linha)+': ' + frase_traduzida+'\n')
    linha = linha+1
  f.close()

def main():
  s = ler(sys.argv[1])
  t = int(s[0])
  s.pop(0)

  traduzir(s)

if __name__ == '__main__':
  main()
