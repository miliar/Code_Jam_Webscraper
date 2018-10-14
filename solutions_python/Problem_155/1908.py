# Python standard library imports made available with the core language.
import fileinput

f = fileinput.input()
cases = int(next(f))

for i in range(1, cases + 1):
    _, audience = next(f).strip().split()
    # print(audience)
    shills = 0
    standing = 0
    for shyness, members in enumerate(audience):
        members = int(members)
        # print(shyness, members, shills, standing)
        if shyness > standing and members > 0:
            shills += shyness - standing
            standing += shills
        standing += members
    print('Case #%i: %i' % (i, shills))
