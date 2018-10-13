# Problem A pancakes - Code jam 2017
# Mitch McAffee
import heapq
from heapq import heapify, heappop
from pprint import pprint


def check_goal(node):
    node = list(node)
    for pancake in node:
        if pancake == '-':
            return False
    return True


def flip_one_pancake(pancake):
    if pancake == '+':
        return '-'
    else:
        return '+'


def flip_pancakes(pancakes, length, starting_position):
    """
    Flip the pancakes (- -> +) && (+ -> -)
    :param pancakes:
    :param length:
    :param starting_position:
    :return:
    """
    for i in range(length):
        position = starting_position + i
        pancakes[position] = flip_one_pancake(pancakes[position])
    return pancakes


def get_neighbors(pancakes, k):
    """
    Return the possible neighbors of the current node
    :param pancakes:
    :param k:
    :return:
    """
    pancakes_list = list(pancakes)
    neighbors = []
    # Iteratively attempt a flip at every possible position
    for i in range(len(pancakes_list) + 1 - k):
        temp_pancakes = pancakes_list.copy()
        new_neighbor = flip_pancakes(temp_pancakes, k, i)
        neighbors.append(''.join(new_neighbor))
    # print(neighbors)
    return neighbors


def uniform_cost_search(pancakes, k):
    frontier = [(pancakes, [])]
    explored = set()
    while frontier:
        node, path = heapq.heappop(frontier)
        # If it has been explored and has a lower cost then bail
        if node not in explored:
            explored.add(node)
            # Update the path
            path += [node]
            # Return the path if we are at the goal
            if check_goal(node):
                return len(path) - 1
            for neighbor in get_neighbors(node, k):
                if ''.join(neighbor) not in explored:
                    heapq.heappush(frontier, (''.join(neighbor), path))
    return None  # No possible route was found


if __name__ == '__main__':
    # Read in the input
    input_size = int(input())
    pancake_lists = []
    for i in range(0, input_size):
        cur_input = input()
        pancakes, k = [s for s in cur_input.split(" ")]  # Read in a list of boolean - or +
        k = int(k)
        pancake_lists.append({'pancake': pancakes, 'k': k})

    index = 1
    for i in pancake_lists:
        # Do the search for each set of pancakes
        result = uniform_cost_search(i['pancake'], i['k'])
        if result is None:
            result = 'IMPOSSIBLE'
        print('Case #' + str(index) + ': ' + str(result))
        index += 1

