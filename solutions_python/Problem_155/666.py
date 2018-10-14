T = int(raw_input())
for i in range(T):
    total_up = 0
    need = 0
    raw = raw_input().split(" ")
    max_shynes = int(raw[0])
    info = raw[1]
    for shynes in range(max_shynes+1):
        if total_up < shynes and int(info[shynes]) != 0 :
            need += shynes - total_up
            total_up += need
        total_up += int(info[shynes])
    print "Case #"+str(i+1)+": "+str(need)