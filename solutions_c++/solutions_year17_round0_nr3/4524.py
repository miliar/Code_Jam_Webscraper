#include <stdio.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

string s;
int n, t, k;
vector<int> nums;

int main()
{
    freopen("/Users/aleksandra/Documents/problems/-/C-small-2-attempt0.in", "r", stdin);
    freopen("/Users/aleksandra/Documents/problems/-/C-small-2-attempt0.out", "w", stdout);
    cin >> t;

    for (int j = 0; j < t; ++j)
    {
        cin >> n >> k;
        priority_queue<int> intervals;
        intervals.push(n);
        for (int i = 0; i < k - 1; ++i)
        {
            int cur = intervals.top();
            intervals.pop();
            intervals.push((cur - 1) / 2);
            intervals.push(cur / 2);
        }

//        nums.clear();
//        cin >> n >> k;
//        int tmp = k;
//        while(tmp != 1)
//        {
//            nums.push_back(tmp);
//            tmp /= 2;
//        }
//        int l = 0;
//        int r = n + 1;
//        int curPos = (n + 1) / 2;
//
//        int prev = 1;
//        for (int i = nums.size() - 1; i >= 0 ; --i)
//        {
//            if ((nums[i] == prev * 2 && (curPos - l >= r - curPos)) || ((nums[i] == prev * 2 + 1) && (curPos - l < r - curPos))) r = curPos;
//            else l = curPos;
//
//            curPos = (r - l) / 2 + l;
//
//            prev = nums[i];
//        }
        int cur = intervals.top();
        cout <<  "Case #" << j + 1 << ": " << cur / 2 << " " << (cur - 1) / 2 << endl;

    }

}
