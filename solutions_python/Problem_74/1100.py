import sys

def parse(file_name):
    in_data = open(file_name).readlines()
    fixed_data = [line.strip() for line in in_data]
    return int(in_data[0]), fixed_data[1:]

def parse_orders(test_data):
    command_list = test_data.split()[1:]
    orders = {}
    orders['O'] = []
    orders['B'] = []
    sequence = []
    while len(command_list) > 0:
        color, position = command_list.pop(0), command_list.pop(0)
        orders[color].append(position)
        sequence.append((color, position))
    return orders, sequence

class Bot:

    def __init__(self, color, orders):
        self.color = color
        self.orders = orders
        self.current_order = 0
        if len(self.orders) > 0:
            self.current_order = int(self.orders.pop(0))
        self.position = 1
        #raw_input(self)

    def __str__(self):
        return "Bot: " + self.color + "\nPosition: " + str(self.position) + "\nOrders: " + str(self.orders) + "\nCurrent order: " + str(self.current_order)

    def tick(self, color, position):
        if color == self.color and position == self.position:
           if len(self.orders) > 0:
               self.current_order = int(self.orders.pop(0)) 
           #print self.color, self.position, "Push"
           return True
        else:
           if self.position > self.current_order:
               self.position = self.position - 1
           if self.position < self.current_order:
               self.position = self.position + 1
        #raw_input(self)
        return False
 
no_of_tests, data = parse(sys.argv[1])
case = 0
for test_data in data:
    case = case + 1
    #print "\n\n" + str(test_data)
    orders, sequence = parse_orders(test_data)
    bots = []
    for color in orders.keys():
        bot = Bot(color, orders[color])
        bots.append(bot)
    ticks = 0
    while len(sequence) > 0:
        color, position = sequence.pop(0)
        pushed = False
        while not pushed:
            ticks = ticks + 1 
            #print "\n","Time:",ticks
            for bot in bots:
                move = bot.tick(color, int(position))
                pushed = pushed or move

    print "Case #" + str(case) + ": " + str(ticks)


