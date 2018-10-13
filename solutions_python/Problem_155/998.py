from sys import stdin

cases = int(stdin.readline())
for i in range(1,cases+1):
    maximum, audience = stdin.readline().strip().split()
    audience = [int(x) for x in audience]
    stand = 0
    invite = 0
    for shyness,total in enumerate(audience):
        if total == 0: continue

        need = 0
        if shyness > 0 and stand < shyness:
            need = shyness-stand
            invite += need

        stand += total+need
    print("Case #{0}: {1}".format(i,invite))

