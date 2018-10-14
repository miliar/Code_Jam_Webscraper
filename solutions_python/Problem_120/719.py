import math
f = open('A-small-attempt0.in')
numTestCase = f.readline()
answers = []

for i in xrange(int(numTestCase)):
    radius, milliPaint = f.readline().split()
    radius = int(radius)
    milliPaint = int(milliPaint)
    numCircles = 0
    circleCenter = (int(radius) ** 2)
    nextCircleCenter = ((int(radius) + 1) ** 2)
    while milliPaint > 0:
        if milliPaint >= nextCircleCenter - circleCenter:
            milliPaint -= nextCircleCenter - circleCenter
            circleCenter = ((int(radius) + 2) ** 2)
            nextCircleCenter = ((int(radius) + 3) ** 2)
            radius += 2
            numCircles += 1
        else:
            break
    answers.append('Case #{}: {}'.format(i + 1, numCircles))
            

f.close()
f = open('A-small-attempt0.txt', 'w')
for i in answers:
    f.write(i)
    f.write('\n')
f.close()
