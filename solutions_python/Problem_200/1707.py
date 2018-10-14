# Problem B: Tidy Numbers: Smoll Input


# Tidy: when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order.
# Some examples of this are 8, 123, 555, and 224488.

# Not tidy: Numbers that do not have this property,  20, 321, 495 and 999990


# Limits 1 <= T <= 100
# Small dataset: 1 <= N <= 1000

def tidy_func(user):
    previous_val = 0
    new_num = ""
    for i in range(len(user)):
        current_val = int(user[i])
        if current_val < previous_val: # drop
            new_num += user[0:i-1]
            difference = len(user) - i
            special = (10 + previous_val -1) % 10
            new_num += str(special)
            new_num += "9" * difference
            return new_num, False
        else:
            previous_val = current_val
            
    return user, True


def recent_tidy_func(user):
    current_user = user
    while True:
        current_user, flag = tidy_func(current_user)
        if flag == True:
            break
    return current_user
        
        

test_cases = int(input(""))

for tree in range(test_cases):
    user = str(input(""))
    clean_int = int(recent_tidy_func(user))
    display_me = str(clean_int)
    print("Case #"+ str(tree+1) + ": "+ display_me)








