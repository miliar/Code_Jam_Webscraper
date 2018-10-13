'''
Created on Apr 11, 2015

@author: Mian Mubasher
'''


#===============================================================================
# Eclipse pydev std input redirect bug workaround
#===============================================================================
import sys
sys.stdin = open('A-large.in')
sys.stdout = open('A-large.out','w')
#------------------------------------------------------------------------------ 

def main():
    test_cases = int(raw_input())
    for test_case_number in range(test_cases):
        test_case_number+=1
        max_shyness, audience = raw_input().split(' ')
        max_shyness = int(max_shyness)
        audience = [int(a) for a in audience]
        people_already_standing = 0
        total_friends_needed = 0
        for shyness_level in range(len(audience)):
            if people_already_standing < max_shyness:
                audience_with_shyness_level = audience[shyness_level]
                aws = audience_with_shyness_level
                friends_needed = 0
                if people_already_standing < shyness_level:
                    friends_needed = shyness_level - people_already_standing
                    total_friends_needed += friends_needed
                people_already_standing += aws + friends_needed
                
            else: break
        print "Case #"+str(test_case_number)+": "+str(total_friends_needed)

if __name__ == '__main__':
    main()