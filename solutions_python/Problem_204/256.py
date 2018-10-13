from math import ceil

def run():
  test_case_count = int(raw_input())  # read a line with a single integer
  for case in range(1, test_case_count + 1):
    ingredients, packages = [int(x.strip()) for x in raw_input().split(" ")]
    grams = [int(x) for x in raw_input().split(" ")]

    package_amounts = []
    for _ in range(ingredients):
      package_amounts.append([int(x) for x in raw_input().split(" ")])

    solution = solve_rat(grams, package_amounts)

    print("Case #{}: {}".format(case, solution))

def solve_rat(gram_reqs, package_sizes):
  # prefill queue
  fullfill_queues = []
  for package_idx, expected_grams in enumerate(gram_reqs):
    package_queue = []
    for package_grams in package_sizes[package_idx]:
      package_min = int(ceil(package_grams / (1.1 * expected_grams)))
      package_max = int(package_grams / (0.9 * expected_grams))

      if package_min <= package_max:
        package_queue.append((package_min, package_max))

    fullfill_queues.append(sorted(package_queue))

    # have 9, package takes 2
    # if I use 90% I have 9 * .9 = 8.1
    # does not work for 4
    # works for 5?
    # 10 * .9 = 9 so yes
    # so really it's
    # expected_grams / 1.1

  kits = 0
  while all(len(queue) > 0 for queue in fullfill_queues):
    fullfill_queues.sort()
    biggest_min = fullfill_queues[-1][0][0]
    can_make = all(biggest_min <= queue[0][1] for queue in fullfill_queues)
    if can_make:
      kits += 1
    # print fullfill_queues, biggest_min, can_make

    for queue in fullfill_queues:
      if can_make or biggest_min > queue[0][1]:
        queue.pop(0)

  return kits

run()
