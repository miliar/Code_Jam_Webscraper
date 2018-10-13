

def friends_to_invite(shyness):
    friends = 0

    for i in range(len(shyness)):
        additional_friends = max(i - sum(shyness[:i]), 0)
        shyness[i] += additional_friends
        friends += additional_friends
    
    return friends


def main():
    num_test_cases = int(input())

    for i in range(num_test_cases):
        shyness = []
        max_shyness, counts = input().split()
        
        max_shyness = int(max_shyness)
        for j in range(max_shyness+1):
            shyness.append(int(counts[j]))

        friends = friends_to_invite(shyness)
        print("Case #{}: {}".format(i+1, friends))


if __name__ == "__main__":
    main()


