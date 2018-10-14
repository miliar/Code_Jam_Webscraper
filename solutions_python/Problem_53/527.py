import string
import sys

def find_snap_th_light(snappers):
    if snappers == 1:
        return 1
    
    snaps = 0
    chain = [0 for i in range(snappers)]
    while True:
        snaps += 1
        flow = True
        for i in range(snappers):
            if not flow:
                break
            else:
                if chain[i]==0:
                    chain[i] = 1
                    if i == snappers-1:
                        return snaps + 1
                    break
                else:
                    chain[i] = 0

def solve(chain, snaps):
    if snaps == 0: return False
    if chain == 1: return (snaps%2!=0)
    if chain > 0:
        #snaps_th = find_snap_th_light(chain)
        snaps_th = 2**chain
        snaps = snaps - (snaps_th - 1) # first snaps
        if snaps < 0: # light is OFF
            return False
        else:
            return (snaps%snaps_th) == 0 # if 0 is ON else is OFF
    
def main():
    file = open(sys.argv[1])
    output = open('result.a', 'w')

    # number of maps
    cases = int(file.readline())

    for index in range(cases):
        # load the height and width
        chain, snap = file.readline().split()
        chain, snap = int(chain), int(snap)
        result = solve(chain, snap)
        template = "Case #%d: %s\n"
        output.write(template%((index+1, "ON" if result else "OFF")))

    output.flush()
    output.close()
    file.close()
    
main()