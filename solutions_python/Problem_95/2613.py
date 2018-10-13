import unittest

from speaking_in_tongues import speak,googlerese, main
from os.path import isfile
from os import remove

class SpeakingInTonguesTest(unittest.TestCase):

    def test_our(self):
        self.assertEquals('our', googlerese('ejp'))

    def test_language(self):
        self.assertEquals('language', googlerese('mysljylc'))

    def test_is(self):
        self.assertEquals('is', googlerese('kd'))

    def test_impossible(self):
        self.assertEquals('impossible', googlerese('kxveddknmc'))

    def test_to(self):
        self.assertEquals('to', googlerese('re'))

    def test_understand(self):
        self.assertEquals('understand', googlerese('jsicpdrysi'))

    def test_out_language_is_impossible_to_understand(self):
        self.assertEquals('our language is impossible to understand', googlerese('ejp mysljylc kd kxveddknmc re jsicpdrysi'))

    def test_there(self):
        self.assertEquals('there', googlerese('rbcpc'))

    def test_are(self):
        self.assertEquals('are', googlerese('ypc'))

    def test_twenty(self):
        self.assertEquals('twenty', googlerese('rtcsra'))

    def test_factorial(self):
        self.assertEquals('factorial', googlerese('wyfrepkym'))

    def test_there_are_tweenty_six_factorial_possibilities(self):
        self.assertEquals('there are twenty six factorial possibilities',googlerese('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'))

    def test_so_it_is_okay_if_you_want_to_just_give_up(self):
        self.assertEquals('so it is okay if you want to just give up', googlerese('de kr kd eoya kw aej tysr re ujdr lkgc jv'))

    def test_assert_alphabet(self):
        self.assertIsNotNone(googlerese('abcdefghijklmnopqrstuvxywz'))

    def test_one_input(self):
        input = '''1
ejp mysljylc kd kxveddknmc re jsicpdrysi'''

        output = 'Case #1: our language is impossible to understand'

        self.assertEquals(output, speak(input))

    def test_full_input(self):
        input = '''3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''

        output = '''Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up'''

        self.assertEquals(output, speak(input))


    def test_main_call(self):
        filename = '/tmp/input.txt'
        if isfile(filename):
            remove(filename)
        input = '''3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''
        file = open(filename, 'w')
        file.write(input)
        file.close()

        main(['./speaking_in_tongues', filename, '/tmp/output.txt'])
        self.assertTrue(isfile('/tmp/output.txt'))
        output_file = open('/tmp/output.txt', 'r')
        output = output_file.read()
        output_file.close()
        expected = '''Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up'''
        self.assertEquals(expected, output)
        if isfile('/tmp/output.txt'):
            remove('/tmp/output.txt')

