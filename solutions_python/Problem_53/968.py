# vim:fileencoding=utf-8

from __future__ import print_function

class Snapper(object):
    def __init__(self):
        self.state = 0 # 0:OFF 1:ON
        self.output = None
        self.powered = False

    def connect_to(self, other_snapper):
        other_snapper.output = self
    
    def flip(self):
        output_previously_powered = False
        if self.state == 1:
            self.state = 0
            if self.output:
                output_previously_powered = self.output.powered
                self.output.powered = False
        else:
            self.state = 1
            if self.output:
                output_previously_powered = self.output.powered
                self.output.powered = True
        return output_previously_powered

    def __str__(self):
        return u"<Snapper state: %s, powered: %s>" % (self.state, self.powered)

class SnapperChain(object):
    def __init__(self, num=0):
        self.root = None
        for i in range(num):
            self.add(Snapper())

    def add(self, snapper):
        if not self.root:
            self.root = snapper
            self.last_snapper = self.root
            self.root.powered = True
        else:
            snapper.connect_to(self.last_snapper)
            self.last_snapper = snapper

    def snap(self):
        snapper = self.root
        # flip state
        while snapper:
            if snapper.powered:
                snapper.state = -1 * (snapper.state - 1)
                snapper = snapper.output
            else:
                snapper = None
        # adjust power
        snapper = self.root
        while snapper:
            if snapper.powered and snapper.output:
                if snapper.state == 1:
                    snapper.output.powered = True
                elif snapper.state == 0:
                    snapper.output.powered = False
                snapper = snapper.output
            else:
                if snapper.output:
                    snapper.output.powered = False
                    snapper = snapper.output
                else:
                    snapper = None

    def check(self):
        return self.last_snapper.powered and self.last_snapper.state == 1

    def dump(self):
        snapper = self.root
        while snapper:
            print(snapper)
            snapper = snapper.output

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("[usage] %s [input file]" % sys.argv[0])
        sys.exit(0)

    input = None
    with open(sys.argv[1], 'r') as f:
        t = int(f.next().strip())
        for i in range(t):
            n, k = map(lambda e: int(e), f.next().strip().split())
            print("Case #%d: " % (i+1), end="")
            
            if k == 0:
                print("OFF")
                continue

            sc = SnapperChain(n)
            checked = False
            for j in range(k):
                sc.snap()
                if sc.check():
                    if (k + 1) % (j + 2) == 0:
                        print("ON")
                    else:
                        print("OFF")
                    checked = True
                    break
            if not checked:
                if sc.check():
                    print("ON")
                else:
                    print("OFF")
