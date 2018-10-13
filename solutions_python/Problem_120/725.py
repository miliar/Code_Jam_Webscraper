def draw(r, t):
    old_r = r
    current_r = r + 1
    req_paint = current_r**2 - old_r**2
    count = 0

    while (t - req_paint) >= 0:
        t = t - req_paint
        count += 1
        old_r = current_r + 1
        current_r = old_r + 1
        req_paint = current_r**2 - old_r**2

    return count

num_cases = int(raw_input())

for case in range(1, num_cases+1):
    eye = raw_input()
    eye = eye.split(" ")

    r = long(eye[0])
    t = long(eye[1])

    print "Case #%d: %d" % (case, draw(r,t))