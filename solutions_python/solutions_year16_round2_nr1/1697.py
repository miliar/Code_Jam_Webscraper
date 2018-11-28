# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 11:06:51 2016

@author: Dane
"""

numbers =['ZERO','ONE','TWO', 'THREE', 'FOUR', 'FIVE', \
            'SIX', 'SEVEN', 'EIGHT', 'NINE']

def rec(nums, word, order):
    if len(word) == 0:
        return order
    else:
        if len(nums) == 0:
            return []
        else:
            nn = list(numbers[nums[0]])
            if not sub_list(nn, word):
                a = []
                b = []
            else:
                a = rec(nums, removel(nn, word), order + [nums[0]])
                b = rec(nums[1:], removel(nn, word), order + [nums[0]])
  

            c =  rec(nums[1:], word, order)
            if len(a) >= len(b) and len(a) >= len(c):
                return a
            elif len(a) <= len(b) and len(b) >= len(c):
                return b
            else:
                return c
                
                
def sub_list(a,c):
    b = []
    b += c
    for x in a:
        if x in b:
            b.remove(x)
        else:
            return False
    return True

def removel(a,b):
    c= []
    c += b
    for x in a:
        c.remove(x)
    return c
    
def get_numbers(word):
    nums = []
    for num in numbers:
        new_word = []
        new_word += word
        cc = len(num)
        count = 0
        for x in num:
            if x in new_word:
                new_word.remove(x)
                count += 1
            else:
                break
        if count == cc:
            nums += [numbers.index(num)]
    return nums           

def find_order(nums, word):
    for x in range(len(nums)):
        new_word = []
        new_word += removel(list(numbers[nums[x]]), list(word))
        order = [nums[x]]
        for y in range(x, len(nums)):
            nn = list(numbers[nums[y]])
            while sub_list(nn,new_word):
                order += [nums[y]]
                new_word = removel(nn, new_word)
                if not sub_list(nn,new_word):
                    break
            if new_word == []:
                return order
        if new_word == []:
                return order
                
                    
def main():
    output = "Case #{}: {}"
    for x in range(int(raw_input())):
        word = raw_input().strip()
        wl = list(word)
        nums =  get_numbers(wl)
        a = rec(nums, wl,[])
        order = "".join([str(z) for z in a])
        print output.format((x+1),order)

main()