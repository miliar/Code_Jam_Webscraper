num_of_loops = int(input())

def solution(case):
    case = case.split()
    n = case[0]
    k = case[1]
    result = "0" * int(n)
    #print(result)
    longest_empty_chain = 0
    longest_empty_chain_index = 0
    for i in range(int(k)):
        counter = 0
        longest_empty_chain = 0
        longest_empty_chain_index = 0
        result = result.replace("x", "1")
        result = result.split("1")
        while (counter < len(result)):
            if (len(result[counter]) > longest_empty_chain):
                longest_empty_chain = len(result[counter])
                longest_empty_chain_index = counter
            counter += 1
        if (len(result[longest_empty_chain_index]) & 1):
            index = len(result[longest_empty_chain_index])//2 + 1
        else:
            index = len(result[longest_empty_chain_index])//2
        #print(result, longest_empty_chain, longest_empty_chain_index)
        result[longest_empty_chain_index] = result[longest_empty_chain_index][:index-1] + "x" + result[longest_empty_chain_index][index:]
        #print(result, longest_empty_chain, longest_empty_chain_index)
        #print("len"+str(len(result) - 1))
        result = "1".join(result)
        #print(result)
    index = result.find("x")
    counter = index-1
    left = 0
    right = 0
    cont = True
    while (counter >= 0 and cont):
        if (result[counter] == "0"):
            left += 1
        else:
            cont = False
        counter -= 1
    cont = True
    counter = index+1
    while (counter < len(result) and cont):
        if (result[counter] == "0"):
            right += 1
        else:
            cont = False
        counter += 1
    """
    left = 0
    right = 0
    cont = True
    counter = len(index[0]) - 1
    while (counter >= 0 and cont):
        if (index[0][counter] == "0"):
            left += 1
        else:
            cont = False
        counter -= 1"""
    #print(index, right, left)
    return (str(right) + " " + str(left))

for i in range(num_of_loops):
    print("Case #"+str(i+1)+": " + solution(input()))

