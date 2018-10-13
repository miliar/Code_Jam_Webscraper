def magic_trick(tokens):
  token = iter(tokens)
  cases = int(next(token))
  for case in range(cases):
    row = int(next(token))
    first = [{int(next(token)) for i in range(4)} for j in range(4)]
    col = int(next(token))
    second = [{int(next(token)) for i in range(4)} for j in range(4)]
    answers = first[row-1] & second[col-1]
    if len(answers) == 0:
      yield case+1, "Volunteer cheated!"
    elif len(answers) == 1:
      yield case+1, answers.pop()
    else:
      yield case+1, "Bad magician!"

if __name__ == "__main__":
  import sys
  for case, result in magic_trick(sys.stdin.read().split()):
    print("Case #%s: %s" % (case, result))
