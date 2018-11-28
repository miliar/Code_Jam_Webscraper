import sys

def log(msg):
    print >> sys.stderr, msg

class Bot(object):
    def __init__(self, name, commands = None, position = 1):
        self.name = name
        self.commands = commands or []
        self.position = position
        
    def update(self, time):
        try:
            cmd = self.commands[0]
        except IndexError:
            return
        
        getattr(self, 'handle_' + type(cmd).__name__)(cmd, time)
        
        if cmd.is_completed:
            self.commands.pop(0) 
        
    def handle_PushButtonCommand(self, cmd, time):
        if self.position != cmd.button:
            self._move_to_button(cmd.button)
        elif not cmd.dependency or (cmd.dependency.is_completed and cmd.dependency.completed_at < time):
            self._push_button()
            cmd.mark_as_completed(time)
    
    def _push_button(self):
        log("%s pushes button %s." % (self.name, self.position))
        
    def _move_to_button(self, button):
        if self.position == button:
            log("%s stays at button %s." % (self.name, self.position))
        else:
            self.position += 1 if self.position < button else -1
            log("%s moves to button %s." % (self.name, self.position))
        

class Command(object):
    def __init__(self):
        self.is_completed = False
        
    def mark_as_completed(self, time):
        self.is_completed = True
        self.completed_at = time
    
    
class PushButtonCommand(Command):
    def __init__(self, button, dependency = None):
        super(PushButtonCommand, self).__init__()
        self.button = button
        self.dependency = dependency
    

def main(input, output):
    cases_count = int(input.readline())
    for i in xrange(cases_count):
        case_id = i+1
        
        bots = {
            'O': Bot(name = 'Orange'),
            'B': Bot(name = 'Blue'),
        }
        
        case = input.readline()
        case = iter(case.split())
        prev_cmd = None
        for j in xrange(int(case.next())):
            bot = bots[case.next()]
            button = int(case.next())
            cmd = PushButtonCommand(button, dependency = prev_cmd)
            bot.commands.append(cmd)
            prev_cmd = cmd
            
        time = 0
        while True:
            time += 1
            log("Time is %s" % time)
            for bot in bots.values():
                bot.update(time)
            if all(not bot.commands for bot in bots.values()):
                break
        
        print >> output, 'Case #%s: %s' % (case_id, time)

if __name__ == '__main__':
    if '-q' in sys.argv:
        log = lambda msg: None
        sys.argv.remove('-q')
    if len(sys.argv) > 0:
        input_path = sys.argv[1]
    else:
        input_path = 'example.txt'
    with file(input_path) as input:
        main(input, sys.stdout)
    