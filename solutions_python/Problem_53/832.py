#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from unittest import TestCase, TestLoader, TextTestRunner
from snapper import SnapToStateTransformer, StateToPowerTransformer

class TestSnapToStateTransformer(TestCase):
    def test_change_state_one_off_device(self): 
        self.__assertSnapToStateWorks(
                         n=1, 
                     power=(1,), 
                     state=(0,), 
            expected_state=[1,]
        )

    def test_change_state_one_on_device(self):
        self.__assertSnapToStateWorks(
                         n=1, 
                     power=(1,), 
                     state=(1,), 
            expected_state=[0,]
        )

    def test_change_state_two_off_devices_1(self): 
        self.__assertSnapToStateWorks(
                         n=2, 
                     power=(1, 0), 
                     state=(0, 0), 
            expected_state=[1, 0]
        )

    def test_change_state_two_off_devices_2(self):
        self.__assertSnapToStateWorks(
                         n=2, 
                     power=(1, 1), 
                     state=(0, 0), 
            expected_state=[1, 1]
        )

    def test_change_state_two_on_devices_1(self): 
        self.__assertSnapToStateWorks(
                         n=2, 
                     power=(1, 0), 
                     state=(1, 1), 
            expected_state=[0, 1]
        )

    def test_change_state_two_on_devices_2(self): 
        self.__assertSnapToStateWorks(
                         n=2, 
                     power=(1, 1), 
                     state=(1, 1), 
            expected_state=[0, 0]
        )

    def test_change_state_one_on_one_off_devices_1(self): 
        self.__assertSnapToStateWorks(
                         n=2, 
                     power=(1, 0), 
                     state=(1, 0), 
            expected_state=[0, 0]
        )

    def test_change_state_one_on_one_off_devices_2(self): 
        self.__assertSnapToStateWorks(
                         n=2, 
                     power=(1, 1),
                     state=(1, 0), 
            expected_state=[0, 1]
        )

    def test_change_state_one_on_one_off_devices_3(self): 
        self.__assertSnapToStateWorks(
                         n=2, 
                     power=(1, 0),
                     state=(0, 1), 
            expected_state=[1, 1]
        )

    def test_change_state_one_on_one_off_devices_4(self): 
        self.__assertSnapToStateWorks(
                         n=2, 
                     power=(1, 1),
                     state=(0, 1), 
            expected_state=[1, 0]
        )

    def test_change_state_many_different_devices(self): 
        self.__assertSnapToStateWorks(
                         n=14, 
                     power=(1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     state=(0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1), 
            expected_state=[1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1]
        )

    def __assertSnapToStateWorks(self, n, power, state, expected_state):
        transformer = SnapToStateTransformer()
        new_state = transformer.change_state(n, power, state)

        self.assertEqual(new_state, expected_state)

class TestStateToPowerTransformer(TestCase):
    def test_change_power_one_powered_device_1(self): 
        self.__assertStateToPowerWorks(
                         n=1,
                     state=(0,),
                     power=(1,),
            expected_power=[1,]
        )

    def test_change_power_one_powered_device_2(self): 
        self.__assertStateToPowerWorks(
                         n=1,
                     state=(1,),
                     power=(1,),
            expected_power=[1,]
        )

    def test_change_power_two_powered_devices_1(self): 
        self.__assertStateToPowerWorks(
                         n=2,
                     state=(0, 1),
                     power=(1, 1),
            expected_power=[1, 0]
        )

    def test_change_power_two_powered_devices_2(self): 
        self.__assertStateToPowerWorks(
                         n=2,
                     state=(1, 1),
                     power=(1, 1),
            expected_power=[1, 1]
        )

    def test_change_power_two_powered_devices_3(self): 
        self.__assertStateToPowerWorks(
                         n=2,
                     state=(1, 0),
                     power=(1, 1),
            expected_power=[1, 1]
        )

    def test_change_power_one_powered_one_not_devices_1(self): 
        self.__assertStateToPowerWorks(
                         n=2,
                     state=(1, 0),
                     power=(1, 0),
            expected_power=[1, 1]
        )

    def test_change_power_one_powered_one_not_devices_2(self): 
        self.__assertStateToPowerWorks(
                         n=2,
                     state=(1, 1),
                     power=(1, 0),
            expected_power=[1, 1]
        )

    def test_change_power_one_powered_one_not_devices_3(self): 
        self.__assertStateToPowerWorks(
                         n=2,
                     state=(0, 1),
                     power=(1, 0),
            expected_power=[1, 0]
        )

    def test_change_power_many_different_devices_1(self): 
        self.__assertStateToPowerWorks(
                         n=8,
                     state=(1, 1, 1, 1, 1, 0, 1, 0),
                     power=(1, 1, 1, 0, 0, 0, 0, 0),
            expected_power=[1, 1, 1, 1, 1, 1, 0, 0]
        )

    def test_change_power_many_different_devices_2(self): 
        self.__assertStateToPowerWorks(
                         n=8,
                     state=(1, 0, 1, 0, 1, 0, 1, 0),
                     power=(1, 1, 1, 1, 1, 1, 1, 1),
            expected_power=[1, 1, 0, 0, 0, 0, 0, 0]
        )

    def __assertStateToPowerWorks(self, n, state, power, expected_power):
        transformer = StateToPowerTransformer()
        new_power = transformer.change_power(n, state, power)

        self.assertEqual(new_power, expected_power)

if __name__ == "__main__":
    suite1 = TestLoader().loadTestsFromTestCase(TestSnapToStateTransformer)
    TextTestRunner(verbosity=2).run(suite1)
    suite2 = TestLoader().loadTestsFromTestCase(TestStateToPowerTransformer)
    TextTestRunner(verbosity=2).run(suite2)