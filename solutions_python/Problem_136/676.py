from code_jam import solve_with

@solve_with()
def cookies(tokens):
    farm_cost, farm_boost, goal = tokens.next_many_tokens(3, float)

    def time_until(goal, cps):
        return goal / cps

    def should_buy_farm_given(cps):
        #Time until goal without buying
        time_to_goal_no_buy = time_until(goal, cps)

        #Time until farm
        time_to_farm = time_until(farm_cost, cps)

        #Time until goal after buysing
        time_to_goal_after_farm = time_until(goal, cps + farm_boost)

        #Time until goal with buying
        time_to_goal_with_farm = time_to_farm + time_to_goal_after_farm

        return time_to_goal_with_farm < time_to_goal_no_buy

    cps = 2
    t = 0

    while should_buy_farm_given(cps):
        t += time_until(farm_cost, cps)
        cps += farm_boost

    t += time_until(goal, cps)

    return "{:.7f}".format(t)
