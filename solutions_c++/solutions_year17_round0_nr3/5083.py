#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <unordered_map>
#include <stdint.h>
using namespace std;

struct Solution
{
    void solve(int test)
    {
        int n, k;
        cin >> n >> k;
        multiset<int> q;
        q.insert(n);
        for (int i = 0; i < k - 1; ++i)
        {
            int cur = *q.rbegin() - 1;
            q.erase(--q.end());
            q.insert(cur / 2);
            q.insert(cur - cur / 2);
        }
        int ans = *q.rbegin() - 1;
        cout << "Case #" << test << ": " << ans - ans / 2 << " " << ans / 2 << endl;
    }
};

int main(void)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        Solution().solve(i + 1);
    }
    return 0;
}