normals=[]
surprisings=[]


for judge1 in range(11):
  for judge2 in range(11):
    for judge3 in range(11):
      score=(judge1,judge2,judge3)
      spread=max(score)-min(score)
      if spread < 2:
        normals.append(score)
      if spread == 2:
        surprisings.append(score)

normal_sums = lambda p: [sum(x) for x in normals if max(x) >= p]
surprising_sums =lambda p: [sum(x) for x in surprisings if max(x) >= p]

f=open("B-large.in").readlines()

#f="""4
#3 1 5 15 13 11
#3 0 8 23 22 21
#2 1 1 8 0
#6 2 8 29 20 8 18 18 21""".splitlines()

def go():
  i_lines = [x.strip() for x in f]
  case_count=int(i_lines[0])
  i_lines = i_lines[1:]
  assert case_count==len(i_lines)
  numbers = [[int(x) for x in aline.split(' ')] for aline in i_lines]
  casenumber = 1
  the_results=[]
  for case in numbers:
    num_of_googlers = case[0]
    surprising_number = case[1]
    p = case[2]
    googlers = case[3:] 
    #print "for %i with %i surpising who had %i for the average %f total %i average %f"  %(num_of_googlers, surprising_number, p, sum(googlers)/float(num_of_googlers)/3.0, sum(googlers), sum(googlers)/float(num_of_googlers))
    normal_googs = [x in normal_sums(p) for x in googlers]
    surprising_googs = [x in surprising_sums(p) for x in googlers]
    #print normal_googs
    #print surprising_googs
    corrections=0
    results=[]
    for x in range(len(normal_googs)):
      if normal_googs[x]:
        results.append(True)
      else:
        if surprising_number > corrections:
          if surprising_googs[x]:
            results.append(True)
            corrections += 1
          else:
            results.append(False)
        else:
          results.append(False)
    thecount = len([x for x in results if x])
    the_results.append("Case #%i: %i" % (casenumber, thecount))
    casenumber += 1
  return '\n'.join(the_results)

open('B-large.out','w').write(go())





