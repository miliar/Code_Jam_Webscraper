from StdSuites.AppleScript_Suite import result

def good_read(f):
    return f.readline().replace("\n","")

def read_line_and_split(f):
    return good_read(f).split(" ")

def read_int_line(f):
    return int(good_read(f))

def read_int_arr(f):
    return map(int, read_line_and_split(f))

#==========================

class Order(object):
    def __init__(self,bot,button,index):
        self.bot = bot
        self.button = button
        self.index = index
        self.to_go = None

    def __repr__(self):
        return "[Bot: %s But: %s Ind: %d Go: %s]" % (self.bot, self.button, self.index, str(self.to_go))

    def __str__(self):
        return self.__repr__()


def main(inf, outf):
    fr = open(inf)
    fw = open(outf, 'w')
    T = read_int_line(fr)
    for i in range(T):
        buttons_list = read_bots_orders(fr)
#        print "\n-----------\nCase #%d" % (i + 1)
        res = "Case #%d: %d\n" % (i+1, result(buttons_list))
        fw.write(res)
    fw.close()
    fr.close()

def read_bots_orders(f):
#    buttons_list = {"O":[],"B":[]}
    buttons_list = []
    items = read_line_and_split(f)
    buttons = int(items.pop(0))
    for i in range(buttons):
        buttons_list.append(Order(items[i*2], int(items[i*2+1]), i))
    return buttons_list

def other_bot(bot):
    return "O" if bot == "B" else "B"

def result(buttons_list):
    positions = {"O":1, "B":1}
    first = buttons_list.pop(0)
    first.to_go = abs(positions[first.bot] - first.button)+1
    stack = [first]
    time = 0
    while buttons_list or stack:
        if len(stack) < 2 and buttons_list:
            for i in range(len(buttons_list)):
                order = buttons_list[i]
                if not stack or order.bot != stack[0].bot:
                    temp = buttons_list.pop(i)
                    temp.to_go = abs(positions[order.bot]-order.button)+1
                    stack.append(temp)
                    break

        stack.sort(key=lambda a:a.index)
        first, second = stack[0], stack[1] if len(stack) > 1 else None
        if first.to_go > 0:
            time += first.to_go
            positions[first.bot] = first.button

            if second:
                second.to_go -= first.to_go
                if second.to_go <= 0:
                   second.to_go=1
                    
        del stack[0]
        
    if stack:
        time+=stack[0].to_go
    return time

if __name__ == "__main__":
    main("A-large.in","but_result.txt")
#    main("but_trust_test.txt","but_result.txt")