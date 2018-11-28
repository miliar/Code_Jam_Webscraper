# -*- coding: utf-8 -*-


def main():
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    a_alpha = ['y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q', ' ']
    source = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
          'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
          'de kr kd eoya kw aej tysr re ujdr lkgc jv']
    text = ['our language is impossible to understand',
            'there are twenty six factorial possibilities',
            'so it is okay if you want to just give up']
    text_map = {}
    for sl, tl in zip(source, text):
      for sc, tc in zip(sl, tl):
        text_map[sc] = tc
    text_map = {}
    for i, v in zip(a_alpha, alpha):
      text_map[i] = v
    f = open('A-small-attempt3.in', 'r')
    lines = f.readlines()
    ans = []
    for line in lines[1:]:
      ansline = ''
      for c in line:
        if c == '\n':
          continue
        ansline += text_map[c]
      ans.append(ansline)
    for n, l in enumerate(ans):
      print 'Case #' + str(n + 1) + ': ' + l

if __name__ == '__main__':
    main()

