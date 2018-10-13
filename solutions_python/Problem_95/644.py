table = dict()

while True:
    enc = raw_input("Encrypt Message: ")
    dec = raw_input("Decoded Message: ")
    
    if dec:
        table.update(dict([(e, d) for e, d in zip(enc, dec)]))
        print table
        print table['e']
    else:
        break

print ""
print "--- Answer ---"
print ""

n = int(raw_input())

for i in range(n):
    enc = raw_input()
    print "Case #%d:" % (i + 1),
    s = [table.get(i, "?") for i in enc]
    print "".join(s)
