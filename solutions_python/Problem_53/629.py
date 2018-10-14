# The Snapper Chain - Google Code Jam 2010
# by Jonathan Sorce

# Open the text file
snapperin = open("A-large.in", "r")
# define the variable T
T = int(snapperin.readline())

# Upon writing out an example on paper, I discovered that essentially, all
# that is happening every time you snap is counting up in binary.
# for example: in this list of snappers
# [1, 0, 1, 0], the 2nd and 4th snappers are on (the outlet is on the right,
# and the lightbulb on the left). Each snap will increase
# the number in binary by 1. 1011, 1100, 1101, etc.
# It may be difficult to explain, but here goes: Assuming a fully saturated list
# i.e. N ones (in this example I will use 1111, where N is 4)
# , subtract that binary value from K. The new constant
# (K-15) must be evenly divisible by a fully saturated list plus one -
# this is because after 1111 is reached, it will return to 0000 - which
# is the +1. So, simply put:
# if (K-15)%16 == 0: The light will be on. in all other cases it is off. So:

snapperout = open("A-large.out", "w")
for i in range(T):
    values = snapperin.readline().split(" ")
    N = int(values[0])
    K = int(values[1])
    
    # Find the decimal value of the "fully saturated" snappers
    decnum = int("1" * N, 2)

    if (K - decnum)%(decnum + 1) == 0:
        snapperout.write("Case #" + str(i + 1) + ": ON\n")
        
    else:
        snapperout.write("Case #" + str(i + 1) + ": OFF\n")

snapperout.close()
snapperin.close()

raw_input("Press enter to exit. ")
