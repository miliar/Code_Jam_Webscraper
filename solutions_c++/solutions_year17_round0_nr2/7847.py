#include <iostream>
#include <cassert>
#include <vector>
#include <algorithm>
#include <cmath>

std::vector<int> decompose(std::int64_t num)
{
    assert(num > 0);
    std::vector<int> nums;
    nums.reserve(std::log10(num) + 1);
    while (num > 0)
    {
        nums.push_back(num%10);
        num /= 10;
    }
    std::reverse(nums.begin(), nums.end());
    return nums;
}

std::int64_t compose(const std::vector<int>& nums)
{
    assert(!nums.empty());
    std::int64_t num = 0;
    for (int n : nums)
    {
        num = num*10 + n;
    }
    return num;
}

std::int64_t largest_tidy(std::int64_t num)
{
    assert(num >= 0);

    if (num == 0)
    {
        return 0;
    }

    std::vector<int> nums = decompose(num);
    assert(!nums.empty() && nums.front() != 0);

    int first_equal = 0;
    for (int i = 1; i < (int)nums.size(); ++i)
    {
        if (nums[i-1] < nums[i])
        {
            first_equal = i;
        }
        else if(nums[i-1] > nums[i])
        {
            nums[first_equal] -= 1;
            for (int x = first_equal + 1; x < (int)nums.size(); ++x)
            {
                nums[x] = 9;
            }
            return compose(nums);
        }
    }
    return num;
}

int main()
{
    int test_cases = 0;
    std::cin >> test_cases;

    for (int i = 1; i <= test_cases; ++i)
    {
        std::int64_t upper_bound = 0;
        std::cin >> upper_bound;

        std::int64_t lagerst_tidy = largest_tidy(upper_bound);
        std::cout << "Case #" << i << ": " << lagerst_tidy << '\n';
    }
}
