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

int64_t v[9];

struct Solution
{
    void print(int test, int64_t ans)
    {
        cout << "Case #" << test << ": " << ans << endl;
    }

    int64_t k;
    int64_t ans = 0;

    void dfs(int j, int n, int sum)
    {
        if (j == n)
        {
            int64_t cur = 0;
            for (int i = 0; i < n; ++i)
            {
                for (int u = 0; u < v[i]; ++u)
                {
                    cur = cur * 10 + (i + 1);
                }
            }
            if (cur <= k)
            {
                ans = max(ans, cur);
            }
            return;
        }
        for (int i = 0; i <= sum; ++i)
        {
            v[j] = i;
            dfs(j + 1, n, sum - i);
        }
    }

    void solve(int test)
    {
        cin >> k;
        int64_t tmp = k;
        int cnt = 0;
        while (tmp)
        {
            ++cnt;
            tmp /= 10;
        }
        dfs(0, 9, cnt);
        print(test, ans);
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