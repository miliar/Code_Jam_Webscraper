from __future__ import division

with open("cookieclickerlarge.txt", "rb") as fi:
    cases = int(fi.next().strip())
    answers = []
    for t in xrange(cases):
        c, f, x = map(float, fi.next().strip().split())
        rate = 2
        elapsed = 0
        current_cookies = 0
        if x <= c:
            answers.append(x / rate)
        else:
            ramp_up = [0]
            finish = [x / rate]
            while True:
                ramp_up.append(ramp_up[-1] + c / rate)
                rate += f
                finish.append(x / rate)
                if ramp_up[-1] + finish[-1] > ramp_up[-2] + finish[-2]:
                    answers.append(ramp_up[-2] + finish[-2])
                    break

with open("cookieclickerresult.txt", "wb") as g:
    g.write("\n".join(["Case #%s: %0.7f" % (x + 1, answers[x]) for x in xrange(cases)]))

