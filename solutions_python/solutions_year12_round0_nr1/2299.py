import sys

def main(argv):
  if len(argv) < 2:
    print 'no input file'
  input_filename = argv[1]
  f = open(input_filename, 'r')
  f_out = open(input_filename.replace('.in','.out'), 'w')
  num_of_cases = int(f.readline())
  Googlerese_lookup = { # figured this out on a google docs spreadsheet, https://docs.google.com/spreadsheet/ccc?key=0AkmMqJ4OTgTCdGkyVFJha3JjVl9YOGNuRTRGRkF6a3c
    'a':'y',
    'b':'h',
    'c':'e',
    'd':'s',
    'e':'o',
    'f':'c',
    'g':'v',
    'h':'x',
    'i':'d',
    'j':'u',
    'k':'i',
    'l':'g',
    'm':'l',
    'n':'b',
    'o':'k',
    'p':'r',
    'q':'z',
    'r':'t',
    's':'n',
    't':'w',
    'u':'j',
    'v':'p',
    'w':'f',
    'x':'m',
    'y':'a',
    'z':'q'
  }
  for i in range(num_of_cases):
    case_num = i + 1
    text_line = f.readline()
    ans_text = ""
    for letter in text_line:
      if letter == " ":
        ans_text += " "
      elif letter == "\n":
        continue
      else:
        ans_text += Googlerese_lookup[letter]
    ans(f_out, i, ans_text)

def ans(f, case_num, ans_text):
  f.write('Case #%s: %s\n' % (case_num+1, ans_text))

if __name__ == "__main__":
  sys.exit(main(sys.argv))