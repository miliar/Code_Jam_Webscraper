import sys

def build_combine(dCombine, sElement):
   ele1, ele2, ele_com = sElement
   dCombine[ele1] = (ele2, ele_com)
   dCombine[ele2] = (ele1, ele_com)

def build_oppose(dOppose, sElement):
   ele1, ele2 = sElement
   dOppose[ele1] = ele2
   dOppose[ele2] = ele1

def walk_n(d_combine, d_oppose, s_n):
   a_output = []
   for c_n in s_n:
      c_tbi = c_n
      if len(a_output) > 0:
         if a_output[-1] in d_combine:
            if c_tbi is d_combine[a_output[-1]][0]:
               c_tbi = d_combine[a_output[-1]][1]
               a_output.pop()
         if c_tbi in [d_oppose[x] for x in a_output if x in d_oppose]:
            a_output = []
         else:
            a_output.append(c_tbi)
      else:
         a_output.append(c_n)
   return a_output

if __name__ == '__main__':
   nCase = int(sys.stdin.readline())

   for ixCase in xrange(nCase):
      d_combine = dict()
      d_oppose = dict()

      line = sys.stdin.readline().split()
      ixLine = 0

      nC = int(line[ixLine])

      for ixNC in xrange(nC):
         ixLine += 1
         build_combine(d_combine, line[ixLine])

      ixLine += 1
      nD = int(line[ixLine])

      for ixND in xrange(nD):
         ixLine += 1
         build_oppose(d_oppose, line[ixLine])

      print('Case #%d: [%s]' % (ixCase+1, ', '.join(walk_n(d_combine, d_oppose, line[-1]))))

