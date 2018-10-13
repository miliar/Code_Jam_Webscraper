#!/usr/bin/env python
"""
Google Code Jam 2011, qualifying round, Problem A. Bot Trust
"""

from collections import namedtuple
import fileinput
import re
import sys
import unittest

class ButtonSeq(object):
    """A sequence of button presses that includes steps to move between buttons.
    
    A button sequence begins with a button press (step 1), followed by a number
    of steps to the next button, one step to press the button, and so on until
    the last button.
    """
    
    __slots__ = ['bot','first','last','instructions','steps']
    
    def __init__(self, bot, first, last=None, instructions=1, steps=1):
        self.bot = bot
        self.first = first
        self.last = last or first
        self.instructions = instructions
        self.steps = steps
    
    def add(self, button):
        self.steps += abs(button - self.last) + 1
        self.last = button
        self.instructions += 1
    
    def dist_from(self, button):
        return abs(self.first - button)
        
    def steps_from(self, button):
        """Return the number of steps if starting from button."""
        return self.dist_from(button) + self.steps
        
    def astuple(self):
        return tuple(getattr(self, attr) for attr in self.__slots__)
        
    def __eq__(self, other):
        return isinstance(other, ButtonSeq) and self.astuple() == other.astuple()
        
    def __repr__(self):
        return "ButtonSeq(%s,%i,%i,%i,%i)" % self.astuple()
        
BotTestCase = namedtuple('BotTestCase', ['num', 'button_seqs'])

def parse_bot_test(case_num, case_str):
    """
    Parse a raw input line and return a BotTestCase, or None if there are no
    instructions. Raises AssertionErrors for invalid input.
    """
    
    bits = re.split('\s+', case_str)
    assert len(bits) % 2 == 1, "Invalid case %i: wrong number of bits" % case_num
    
    expected_len = int(bits[0])
    if expected_len <= 0:
        return None
    
    seqs = []
    cur_bot = None
    cur_seq = -1
    for bot, button in zip(bits[1::2], map(int, bits[2::2])):
        assert bot in ('O','B'), "Invalid bot %s for %i:%i" % (bot, case_num, i)
        assert 1 <= button <= 100, "Invalid button %i for %i:%i" % (button, case_num, i)
        if cur_bot is None or cur_bot != bot:
            cur_bot = bot
            cur_seq += 1
            seqs.append(ButtonSeq(bot, button))
        else:
            seqs[cur_seq].add(button)
        
    actual_len = sum(map(lambda x: x.instructions, seqs))
    assert expected_len == actual_len, "Invalid case %i: expected %i "\
        "instructions but got %i" % (case_num, expected_len, actual_len) 
        
    return BotTestCase(case_num, seqs)

def perform_bot_test(case):
    """
    Given a set of instructions, determine the minimum number of steps
    required to complete them.
    """
    
    seqs = case.button_seqs
    cur = seqs[0]
    cur_steps = cur.steps_from(1)
    if len(seqs) == 1:
        return cur_steps
    
    pos = { 'O': 1, 'B': 1 }
    total_steps = 0
    
    for s in seqs[1:]:
        pos[cur.bot] = cur.last
        total_steps += cur_steps
        concurrent_moves = min(s.dist_from(pos[s.bot]), cur_steps)
        cur = s
        cur_steps = s.steps_from(pos[s.bot]) - concurrent_moves
    
    return total_steps + cur_steps

def execute_bot_tests(input_iter):
    for i,line in enumerate(input_iter):
        if i == 0:
            num_tests = int(line)
            # TODO: if num_tests > threshold, use multiprocessing to run
            # tests in parallel
        else:
            assert num_tests < 0 or i <= num_tests, "More than %i cases" % num_tests
            case = parse_bot_test(i, line.rstrip())
            if case is None:
                print "Case #%i: 0" % i
            else:
                steps = perform_bot_test(case)
                print "Case #%i: %i" % (i, steps)

if __name__ == '__main__':
    # If there are no arguments, execute as an interactive shell
    if len(sys.argv) == 1:
        def raw_input_iter():
            while True:
                inp = raw_input()
                if inp:
                    yield inp
                else:
                    break
        execute_bot_tests(raw_input_iter())
    else:
        execute_bot_tests(fileinput.input(mode='rU'))

class ParseTestCase(unittest.TestCase):
    def test_one_bot(self):
        test_str = "2 B 2 B 1"
        result = parse_bot_test(1, test_str)
        self.assertIsNotNone(result)
        self.assertEqual(result.num, 1, "wrong case number")
        self.assertEqual(len(result.button_seqs), 1, "wrong number of queues")
        self.assertEqual(result.button_seqs[0], ButtonSeq('B', 2, 1, 2, 3))
        
    def test_both_bots(self):
        test_str = "4 O 2 B 1 B 2 O 4"
        result = parse_bot_test(1, test_str)
        self.assertIsNotNone(result)
        self.assertEqual(result.num, 1, "wrong case number")
        self.assertEqual(len(result.button_seqs), 3, "wrong number of queues")
        self.assertEqual(result.button_seqs[0], ButtonSeq('O', 2, 2, 1, 1),
            "ButtonSeq[0] is incorrect")
        self.assertEqual(result.button_seqs[1], ButtonSeq('B', 1, 2, 2, 3),
            "ButtonSeq[1] is incorrect")
        self.assertEqual(result.button_seqs[2], ButtonSeq('O', 4, 4, 1, 1),
            "ButtonSeq[2] is incorrect")

class PerformTestCase(unittest.TestCase):
    def test_one_bot(self):
        case = parse_bot_test(1, "2 B 2 B 1")
        self.assertEqual(perform_bot_test(case), 4)
        
    def test_both_bots_1(self):
        case = parse_bot_test(2, "3 O 5 O 8 B 100")
        self.assertEqual(perform_bot_test(case), 100)
        
    def test_both_bots_2(self):
        case = parse_bot_test(3, "4 O 2 B 1 B 2 O 4")
        self.assertEqual(perform_bot_test(case), 6)