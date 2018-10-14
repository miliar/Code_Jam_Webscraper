__author__ = 'skumaran'

if __name__ == '__main__':
  num_testcases = int(raw_input())
  for tc in range(1, num_testcases+1):
    # C - Cost for Cookie Farm
    # F - Increment
    # X - Happiness Target
    C, F, X = map(float, raw_input().split())
    #cookies = 0
    #rate = 2
    #time = 0.0
    #print 'Number of Cookies Needed %d' % X
    #print 'Current Production rate: %d and Time %f' % (rate, X / rate)
    #print 'Next Production rate: %d and Time For Next Production Rate %f and Total time = %f' % (rate + F,  C/rate, X /(rate+F))
    # Time to get X in Current production rate.
    # Time to get X in New Production rate.
    # Time to get to new Production Rate.
    # What are you doing?
    # You are increasing your cookie production capability.
    # Till when you should increase?
    # When rate to produce X cookies is faster than buying a next farm and producing.
    # How to calculate buying a next farm and producing factor?
    # Buying a next farm will take C cookies time (C/prev_rate) and X / new_rate
    # first_farm_rate = 2.0, second_farm_rate = 6.0, third_farm_rate = 10.0 and fourth_rate = 14.0
    # >>> X / 14.0 + (first_farm + second_farm + thrid_farm)
    # 526.19047619047615
    # >>> X / 18.0 + (first_farm + second_farm + thrid_farm + fourth_farm)
    # 530.15873015873012
    # Go with two loops
    # First loop, harvest with current farm
    # Second loop, harvest with next farm.

    current_rate = 2
    next_rate = 2 + F

    def get_time_to_rate(rate):
      time = 0.0
      curr_rate = 2.0
      while curr_rate < rate:
        time += (C * 1.0) / curr_rate
        curr_rate = curr_rate + F
      return time

    def get_total_time(rate):
      return X / rate + get_time_to_rate(rate)

    while True:
      x = get_total_time(current_rate)
      y = get_total_time(next_rate)
      if x < y:
        break
      current_rate += F
      next_rate += F

    print 'Case #%d: %.7f' % (tc, x)
