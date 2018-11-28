def calculate_profit(R, k, N, groups):

    assert(N == len(groups))
  
    if sum(groups) <= k:
      # All aboard!
      return sum(groups) * R

    states = {}
    turn = 0
    current = 0
    profit = 0

    # Here we simulate the ride.
    while turn < R:

      if current in states:
        # Deja Vu!  We have a loop: we already started boarding from this state
        # in the past.
        break

      i = 0
      passengers = 0
      while passengers + groups[(current + i) % N]  <= k and i < N:
        # Go ahead, fill the roller coaster!
        passengers += groups[(current + i) % N]
        i += 1
      # roller coaster is full.
      profit += passengers
      next = (current + i) % N
      states[current] = (next, passengers)
      current = next
      turn += 1

    if turn < R:
      # Loop found!
      # Let's calculate it's length and profit
      loop_profit = profit
      loop_start = 0
      turns_in_one_loop = turn
      while current != loop_start:
        # We substract what was earned before the loop started
        loop_profit -= states[loop_start][1]
        loop_start = states[loop_start][0]
        turns_in_one_loop -= 1

      # Now multilpy the loop by the number of loops we can still do
      turns_left = R - turn
      full_loops_left = (turns_left / turns_in_one_loop)
      profit += full_loops_left * loop_profit
      turn += full_loops_left * turns_in_one_loop

      # And add the last turns we still have after all loops were done.
      while turn < R:
        profit += states[current][1]
        current = states[current][0]
        turn += 1

    return profit


if __name__ == "__main__":

  count = int(raw_input())
  for i in range(count):
    R, k, N =  [int(s) for s in raw_input().split(" ")]
    groups = [int(s) for s in raw_input().split(" ")]
    print 'Case #' + str(i+1)  + ': ' + str(calculate_profit(R, k, N, groups))
