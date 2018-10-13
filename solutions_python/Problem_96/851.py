
def go(num_suprises, best_result, total_scores):
    count = 0
    for total_score in total_scores:
        next_best = best_result - 1
        if next_best < 0:
            next_best = 0
        min_total_score = best_result + next_best * 2
        if total_score >= min_total_score:
            # print 'easy:', total_score
            count += 1
        elif num_suprises > 0:
            next_best = best_result - 2
            if next_best < 0:
                next_best = 0
            min_total_score = best_result + next_best * 2
            if total_score >= min_total_score:
                # print 'suprise:', total_score, max_score + min_score * 2
                count += 1
                num_suprises -= 1
    return count

T = int(raw_input())
for i in range(T):
    line = raw_input()
    nums = [int(word) for word in line.split()]
    N, num_suprises, best_result, total_scores = (
        nums[0], nums[1], nums[2], nums[3:])
    print N, num_suprises, best_result, total_scores
    res = go(num_suprises, best_result, total_scores)
    print 'Case #%i: %i' % (i + 1, res)

print go(3, 0, [8, 23, 22, 21])