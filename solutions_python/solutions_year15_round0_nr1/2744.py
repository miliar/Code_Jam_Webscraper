"""
We are given an input that is a mapping of the shyness level to the
number of people of that level who will be there.

11111
01234

1 person of shyness 0 will always stand up
Hence 1 person of shyness 1 will stand up
Hence 1 person of shyness 2 will stand up

09
01

There are 9 people with shyness 1.
i.e. 9 people will stand up, if 1 person stands up.
Hence we need to invite a person

110011
012345

1 person will always stand up, as shyness = 0; standup=1
1 person will stand up as shyness = 1; standup=2
No people of shyness 2 and 3
1 person of shyness 4; standup=2 => we can invite 2 people of the lowest
shyness
1 person of shyness 4; standup=4
1 person of shyness 5; standup=5

Basically, I can always just invite people of shyness level 0 as the effect
will get carried over. The level of the people I invite does not have any
kind of an effect.
"""

def process(vals, caseno):
    count = int(vals[0])
    to_invite = 0

    for shyness, pcount in enumerate(vals[1:]):
        shyness += 1
        pcount  = int(pcount)

        if count >= shyness:
            count += pcount
            continue

        to_invite += (shyness - count)
        count += (shyness - count)
        count += pcount

    print "Case #%d: %d" %(caseno, to_invite)



def main():
    T = input()
    for i in xrange(T):
        x, vals = raw_input().strip().split()
        process(vals, i+1)


if __name__ == '__main__':
    main()
