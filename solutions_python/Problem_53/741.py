class Snapper:
        def __init__(self, devices,  snaps):
            self.n_devices = devices
            self.n_snaps = snaps
            # power state
            self.state_power = [True, ] + [False]*(self.n_devices - 1)
            # on/off state
            self.state_on = [False]*(self.n_devices)
           
       
        def snap(self):
            for i in range(self.n_devices):
                if self.state_power[i]:
                    self.state_on[i] = not(self.state_on[i])
                else:
                    break

            for i in range(1, self.n_devices):
                self.state_power[i] = self.state_power[i-1] and self.state_on[i-1]
                if not(self.state_power[i]):
                    break
           
            #print "on:",  self.state_on
            #print "power: ",  self.state_power
           
        def snap_many(self):
            for n in range(self.n_snaps):
                self.snap()
       
        def is_light(self):
            for i in range(self.n_devices):
                if not(self.state_power[i] and self.state_on[i]):
                    return False
            return True
            #self.state_power[i] = self.state_power[i-1] and self.state_on[i-1]
            #return sum(self.state_power)==sum(self.state_on)==self.n_devices



input = open("input.txt")
input_lines = input.readlines()
data_cases = []
for line in input_lines[1:]:
    data_cases.append([int(k) for k in line.split(" ")])
input.close()

output = open("output.txt","w")
for n_case,case in enumerate(data_cases):
    snapper = Snapper(case[0], case[1])
    snapper.snap_many()
    ONOFF = {True:"ON",False:"OFF"}
    output.write("Case #%s: %s\n" % (n_case+1,ONOFF[snapper.is_light()]))

output.close()