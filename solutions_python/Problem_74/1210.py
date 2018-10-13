#!/usr/bin/python

from collections import deque

def get_next_bot_cmd(command_queue, bot_list, bot_name):
    for i in range(0, len(command_queue)):
        if command_queue[i]['bot'] == bot_name:
            return command_queue[i]

def main():
    input_file = open('data.txt', 'r')

    num_data_sets = int(input_file.readline())

    for sequence_num in range(1, num_data_sets+1):
        bots = [
            {'name': "B", 'position': 1, 'next_cmd': None},
            {'name': "O", 'position': 1, 'next_cmd': None}
        ]

        time = 0

        cmd_queue = deque()

        sequence = input_file.readline()
        sequence_parts = sequence.split(" ")

        for i in range(1, len(sequence_parts)):
            if sequence_parts[i] == "B" or sequence_parts[i] == "O":
                cmd_queue.append({'bot': sequence_parts[i], 'button': int(sequence_parts[i+1])})

        # Get initial commands so the bots can be moving right off the bat.
        for bot in bots:
            bot['next_cmd'] = get_next_bot_cmd(cmd_queue, bots, bot['name'])

        while True:
            if len(cmd_queue) == 0:
                break

            time += 1
            button_pushed_this_turn = False

            for bot in bots:
                if len(cmd_queue) == 0:
                    break

                if cmd_queue[0]['bot'] == bot['name'] and cmd_queue[0]['button'] == bot['position'] and not button_pushed_this_turn:
                    cmd_queue.popleft()
                    button_pushed_this_turn = True
                    bot['next_cmd'] = get_next_bot_cmd(cmd_queue, bots, bot['name'])
                else:
                    if bot['next_cmd'] is None:
                        continue
                    elif bot['next_cmd']['button'] > bot['position']:
                        bot['position'] += 1
                    elif bot['next_cmd']['button'] < bot['position']:
                        bot['position'] -= 1

        print "Case #%s: %s" % (sequence_num, time)

main()