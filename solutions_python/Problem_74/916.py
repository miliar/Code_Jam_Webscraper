import logging
from collections import defaultdict, namedtuple

#logging.basicConfig()
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

__all__ = ('ButtonBot', 'BotRunner')

Action = namedtuple('Action', 'bot_name position')

class ButtonBot(object):
    
    """
    A bot that knows how to 
    change its own position
    or push a button at its
    position.
    """

    def __init__(self, name, actions):

        self.name = name
        self.actions = actions
        self.position = 1

        logger.debug('Initialized bot name {0}'.format(self.name))

    @property
    def next_action(self):
        #return next action this
        #bot will be called upon
        #to do

        try:
            return self.actions[0]
        except IndexError as ex:
            return None

    def press_button(self):
        #remove first task.
        return self.actions.pop(0)
        
    def act(self, current_action):

        action = self.next_action

        #import pdb; pdb.set_trace()

        logger.debug('bot {0} found action {1}'.format(
            self.name, current_action))

        #I'm all done.
        if action == None:
            logger.debug("I'm all done")
            return False

        #I have to shift position
        if self.position < action.position:
            logger.debug("""
            I have to move from position {0} to position {1}, 
            so I'm moving one step to the right.""".format(
                self.position, current_action.position
            ))

            self.position += 1
            return False
        if self.position > action.position:
            logger.debug("""
            I have to move from position {0} to position {1}, 
            so I'm moving one step to the left.""".format(
                self.position, current_action.position
            ))

            self.position -= 1
            return False
    
        #I'm in position
        if self.position == action.position:

            logger.debug("I'm in position.")
    
            #It's my turn to play
            if current_action.bot_name == self.name:
                logger.debug('Pushing button')
                self.press_button()
                return True

            #not my turn
            else:
                logger.debug("It's not my turn")
                return False


class BotRunner(object):

    def __init__(self, actions):
        
        """
        Create bots and parse actions.
        """

        self.bot_actions = defaultdict(list)
        self.all_actions = list()
        self.bots = []

        for raw_action in actions:

            action = Action(*raw_action)

            self.all_actions.append(action)
            self.bot_actions[action.bot_name].append(action)

        self.bots = [ 
            ButtonBot(
                name = bot_name,
                actions = self.bot_actions[bot_name],
            )
            for bot_name in self.bot_actions.keys()
        ]

        logger.debug("""
            Created {num_bots} bots: {keys}.
            I have {num_actions} actions to complete.

        """.format(
            num_bots = len(self.bots), 
            keys = self.bot_actions.keys(),
            num_actions = len(self.all_actions),
        ))

    def run(self):
        
        """
        Execute all actions.
        """
    
        time_elapsed = 0

        for action in self.all_actions:

            action_complete = False

            while not action_complete:

                time_elapsed += 1

                action_complete = any([
                    bot.act(action) 
                    for bot in self.bots
                ])

        return time_elapsed
    

if __name__ == '__main__':

    runner = BotRunner([['O', 2], ['B', 1], ['B', 2], ['O', 4]])
    print runner.run()
