
def main():
  fin = open('A-small-attempt0.in','r')
  fout = open('A-large-practice.out','w')
  test_cases = int(fin.readline())
  for test_case in xrange(test_cases):
    arrangement_one = []
    arrangement_two = []
    ans_one = int(fin.readline())
    for x in xrange(4):
      row = fin.readline().split()
      row = [int(card) for card in row]
      arrangement_one.append(row)
    ans_two = int(fin.readline())
    for x in xrange(4):
      row = fin.readline().split()
      row = [int(card) for card in row]
      arrangement_two.append(row)
    cards = list(set(arrangement_one[ans_one-1]).intersection(set(arrangement_two[ans_two-1])))
    if len(cards)==0:
      op = 'Volunteer cheated!'
    elif len(cards)==1:
      op = str(cards[0])
    elif len(cards)>1:
      op = 'Bad magician!'
    fout.write("Case #%d: %s\n"%(test_case+1,op))
  fin.close()
  fout.close()




if __name__ == '__main__':
  main()