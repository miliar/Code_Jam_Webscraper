#!/usr/bin/python3
class Bot():
  def __init__(self, name):
    self.position = 1
    self.name = name

  def move_toward(self, position):
    if (position < self.position):
      self.position -= 1
    elif (position > self.position):
      self.position += 1


  def __str__(self,):
    return(self.name)

class Order():
  def __init__(self, bot, position):
    self.bot = bot
    self.position = position

  def __str__(self):
    return('Bot: {0}; Pos: {1}'.format(self.bot, self.position))

def parse_orders(line, bot1, bot2):
  orders = []
  # We don't want the first number
  tokens = line.split()[1:]
  for bot_index in range(0, len(tokens), 2):
    # we have the bot index, next one is the button position
    bot_name = tokens[bot_index]
    position = tokens[bot_index+1]
    bot = None
    if (bot_name == bot1.name):
      bot = bot1
    else:
      bot = bot2
    orders.append(Order(bot, int(position)))
  return orders


def push_button(bot, order):
  if (order.bot == bot):
    return(order.position == bot.position)


def move_closer(bot, orders):
  # Find the next order for this bot
  order_for_bot = None
  for order in orders:
    if (order.bot == bot):
      order_for_bot = order
      break

  if (order_for_bot == None):
    return None
  bot.move_toward(order.position)


def play_turn(order_line):
  blue_bot = Bot('B')
  orange_bot = Bot('O')

  # generate order list
  orders = parse_orders(order_line, blue_bot, orange_bot)

  # play the game until we've done very order
  turns = 0
  while(len(orders) > 0):
    turns += 1
    bot_done = None

    # DEBUG
    # for order in orders:
    #   print(order, end='  ')
    # print(blue_bot.position, orange_bot.position)

    # Try a button push
    if push_button(orders[0].bot, orders[0]):
      # We pushed a button!
      bot_done = orders[0].bot
      orders.pop(0)

    # Move the bots closer
    if (bot_done != blue_bot):
      move_closer(blue_bot, orders)
    if (bot_done != orange_bot):
      move_closer(orange_bot, orders)

  return(turns)

def main(problem = ''):
  with open('{0}.out'.format(problem), 'w') as out_file:
    with open('{0}.in'.format(problem), 'r') as in_file:
      num_cases = in_file.readline()
      for case_num, order_line in enumerate(in_file.readlines(), 1):
        result = play_turn(order_line)
        out_file.write('Case #{0}: {1}\n'.format(case_num, result))
