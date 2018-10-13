class RollerCoaster:
    def __init__(self,run_times,max_people,group_size,groups):
        self.run_times = run_times
        self.max_people = max_people
        self.group_size = group_size
        self.groups = groups[:]
        self.queue = groups[:]
        self.queues = {}
        self.profits = []
        self.rides_repeating = False
        self.ride_number = 0
        self.recurring_pattern = [0,0]

    def run(self):
        t_queue = tuple(self.queue)
        # searching for recurring patterns
        if self.ride_number > 0 and self.queues.has_key(t_queue):
            self.recurring_pattern[0] = self.queues[t_queue]            
            self.recurring_pattern[1] = self.ride_number - 1
            self.rides_repeating = True
            return
        
        self.queues[t_queue] = self.ride_number
        self.ride_number += 1
        places_left = self.max_people        
        ride = []
        while True:
            if len(self.queue)>0 and places_left >= self.queue[0]:
                ride.append(self.queue[0])
                places_left -= self.queue[0]
                self.queue = self.queue[1:]
            else:
                break
        
        self.queue = self.queue + ride
        self.profits.append(sum(ride))
    
    def run_until_recur(self):
        while not self.rides_repeating:
            self.run()     
            
    def get_profits(self,rides):
        rides_t = rides - self.recurring_pattern[0]
        recurring_length = self.recurring_pattern[1] - self.recurring_pattern[0] + 1
        profits_recurring = self.profits[self.recurring_pattern[0]:self.recurring_pattern[1]+1]
        
        if self.ride_number!=0:
            return sum(self.profits[:min(rides,self.recurring_pattern[0])]) + \
                   sum(profits_recurring)*(rides_t/recurring_length) +  \
                   sum(profits_recurring[0:(rides_t % recurring_length)])
        else:
            return 0
            
input = open("input_roller_my.txt")
input_lines = input.readlines()
data_cases = []
for l in range(1,len(input_lines)-1):
    if l % 2 == 1:
        data_cases.append([[int(k) for k in input_lines[l].split(" ")], \
                           [int(k) for k in input_lines[l+1].split(" ")]])
input.close()

output = open("output_roller.txt","w")
for n_case,case in enumerate(data_cases):
    print n_case
    roller = RollerCoaster(case[0][0],case[0][1],case[0][2],case[1])
    roller.run_until_recur()
    print "zyski", roller.profits, case[0][0]
    output.write("Case #%s: %s\n" % (n_case+1,roller.get_profits(case[0][0])))

output.close()