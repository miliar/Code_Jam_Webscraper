#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

class  Solution
{
public:
    string StableNeighbors(int n, vector<int>& nums)
    {
        this->n = n;
        colors = "ROYGBV";
        result.clear();
        int red = nums[0], orange = nums[1], yellow = nums[2], green = nums[3], blue = nums[4], violet = nums[5];
        //if ((red + yellow < (n + 1) / 2) || (red + blue < (n + 1) / 2) || (blue + yellow < (n + 1) / 2)) return "IMPOSSIBLE";
        int m = max(red, max(yellow, blue));
        if (m > n / 2) return "IMPOSSIBLE";
        if (calc(nums))
        {
            return result;
        }
        return "IMPOSSIBLE";
    }
private: 
    bool calc(vector<int>& nums)
    {
        if (result.length() == n) return true;
        int index = -1;
        unordered_set<int> candidates;
        for (int i = 0; i < 6; i++)
        {
            if (nums[i] == 0) continue;
            if (!result.empty() && colors[i] == result.back()) continue;
            if (result.length() == n - 1 && colors[i] == result[0]) return false;
            if (index == -1 || nums[i] > nums[index])
            {
                index = i;
                candidates.clear();
                candidates.insert(i);
            }
            else if (nums[i] == nums[index])
            {
                candidates.insert(i);
            }
        }
        for (auto it = candidates.begin(); it != candidates.end(); it++)
        {
            int index = *it;
            result += colors[index];
            nums[index]--;
            if (calc(nums)) return true;
            nums[index]++;
            result.pop_back();
        }
        return false;
    }

    int n;
    string result;
    string colors;
};

void main() {
    int t;
    cin >> t;
    Solution sol;
    for (int i = 1; i <= t; ++i) {
        int n;
        cin >> n;
        vector<int> nums;
        for (int j = 0; j < 6; j++)
        {
            int k;
            cin >> k;
            nums.push_back(k);
        }
        cout << "Case #" << i << ": " << sol.StableNeighbors(n, nums) << endl;
    }
}