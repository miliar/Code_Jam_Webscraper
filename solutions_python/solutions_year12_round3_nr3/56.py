t, T = 0, int(input())
while t != T:
    t += 1

    N, M = tuple(map(int, input().split()))
    boxes = tuple(map(int, input().split()))
    boxes = list(zip(boxes[::2], boxes[1::2]))
    toys = tuple(map(int, input().split()))
    toys = list(zip(toys[::2], toys[1::2]))

    m = 0
    count = 0
    hist = [(count, boxes, toys)]
    while hist:
        count, boxes, toys = hist.pop(0)
        
        if boxes and toys:
            bn, bt = boxes.pop(0)
            tn, tt = toys.pop(0)

            if bt == tt:
                count += min(bn, tn)

                if bn == tn:
                    hist.append((count, boxes[:], toys[:]))
                elif bn < tn:
                    hist.append((count, boxes[:], [(tn-bn,tt)]+toys[:]))
                else:
                    hist.append((count, [(bn-tn,bt)]+boxes[:], toys[:]))
            else:
                hist.append((count, boxes[:], [(tn,tt)]+toys[:]))
                hist.append((count, [(bn,bt)]+boxes[:], toys[:]))
            
        else:
            m = max(m, count)
        
    print("Case #%d:" % t, m)
  
