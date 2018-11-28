'''
Created on May 8, 2010

@author: psyho
'''
import unittest

def theme_park(num_rides, train_size, groups):
    groups_size = len(groups)
    double_groups = groups + groups
    
    cycle_count = [0] * groups_size
    amount_per_cycle = [0] * groups_size
    amount_per_group = [0] * groups_size
    next_group = [None] * groups_size
    
    current_group = 0
    rides_so_far = 0
    amount = 0
    
    found_cycle_size = 0
    
    while rides_so_far < num_rides:
        if not cycle_count[current_group]:
            for i in xrange(groups_size): 
                if cycle_count[i]: cycle_count[i] += 1
            cycle_count[current_group] = 1
            
            sum = groups[current_group]
            idx = current_group + 1
            while sum + double_groups[idx] <= train_size and idx % groups_size != current_group:
                sum += double_groups[idx]
                idx += 1
            
            amount_per_group[current_group] = sum
            next_group[current_group] = idx % groups_size            
            
            for i in xrange(groups_size): 
                if cycle_count[i]: amount_per_cycle[i] += sum
            
            amount += sum
            rides_so_far += 1
            current_group = next_group[current_group]
        else:                        
            if not found_cycle_size: found_cycle_size = cycle_count[current_group]
            remaining_rides = num_rides - rides_so_far            
            repeat_count = remaining_rides // found_cycle_size
            
            if repeat_count:
                amount += repeat_count * amount_per_cycle[current_group]
                rides_so_far += repeat_count * found_cycle_size
            else:
                amount += amount_per_group[current_group]
                rides_so_far += 1
                current_group = next_group[current_group]
    
    return amount


def main():
    T = int(raw_input())
    for i in range(T):
        R, k, N = map(int, raw_input().split())
        groups = map(int, raw_input().split())
        print "Case #%d: %d" % (i+1, theme_park(R, k, groups))

if __name__ == "__main__":
    main()


class Test(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(21, theme_park(4, 6, [1, 4, 2, 1]))
        
    def test_example_2(self):
        self.assertEqual(100, theme_park(100, 10, [1]))
        
    def test_example_3(self):
        self.assertEqual(20, theme_park(5, 5, [2, 4, 2, 3, 4, 2, 1, 2, 1, 3]))

    def test_wrong_output(self):
        self.assertEqual(4405, theme_park(115, 43, [6, 8, 9, 6, 5, 8, 8, 8, 9]))

