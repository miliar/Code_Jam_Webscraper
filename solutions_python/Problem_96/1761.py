# Dancing with googlers
import math

def main():
  in_file = open('input.txt', 'r')
  lines = in_file.readlines()
  in_file.close()

  out_file = open('output.txt', 'w')
  num_cases = int(lines.pop(0)) # We don't really use this...
  case_count = 1
  while lines:
    text = lines.pop(0)
    vals = map(int, text.split())

    googlers = vals.pop(0)
    surprising = vals.pop(0)
    p = vals.pop(0)

    # Generate base 3-tuple of scores for each total, eg,
    # 3 or 4 or 5 -> (1, 1, 1)
    # 6 or 7 or 8 -> (2, 2, 2), etc
    base_scores = [(s, s, s) for s in [math.floor(n/3) for n in vals]]

    # Transform the base scores into the least suprising possible scores
    # (and zip the scores with the expected total while we're at it)
    # also note-worthy: the scores are sorted, so the max element is first
    # and the least element is last
    scores = []
    for (x, y, z), total in zip(base_scores, vals):
      if total % 3 >= 1:
        x += 1
      if total % 3 == 2:
        y += 1
      scores.append(((x, y, z), total))
      print scores[-1]

    gt_p = 0
    for (x, y, z), total in scores:
      if x >= p:
        gt_p += 1
      elif surprising > 0 and p-x == 1 and x < 10 and z > 0 and total % 3 != 1:
        gt_p += 1
        surprising -= 1

    output = "Case #%d: %s\n" % (case_count, gt_p)
    out_file.write(output)
    print output
    case_count += 1


if __name__=="__main__":
  main()
