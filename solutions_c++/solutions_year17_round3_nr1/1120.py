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
#include <deque>
using namespace std;

int64_t mod = 1000ll * 1000ll * 1000ll + 7;

struct Solution
{
    int m_test;
    Solution(int test)
        : m_test(test)
    {
    }

    std::ostream& print()
    {
        cout << "Case #" << m_test << ": ";
        return cout;
    }

    void solve()
    {
        int n, k;
        cin >> n >> k;
        vector<int64_t> r(n), h(n);
        vector<int> id(n);
        for (int i = 0; i < n; ++i)
        {
            cin >> r[i] >> h[i];
            id[i] = i;
        }
        auto get = [&](int i) -> int64_t
        {
            return r[i] * r[i] + 2 * r[i] * h[i];
        };
        vector<vector<int64_t> > dp(n, vector<int64_t>(n));
        int64_t ans = 0;
        for (int i = 0; i < n; ++i)
        {
            int64_t cur = get(i);
            int64_t q = r[i];
            r[i] = 0;
            sort(id.rbegin(), id.rend(), 
                [&](int a, int b)
            {
                return 2 * r[a] * h[a] < 2 * r[b] * h[b];
            });
            for (int j = 0; j < k - 1; ++j)
            {
                cur += 2 * r[id[j]] * h[id[j]];
            }
            ans = max(ans, cur);
            r[i] = q;
        }
        double pi = acos(-1.0);
        print();
        printf("%.9f\n", pi * ans);
    }
};

int main(void)
{
#if 1
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
#if 1
    int n;
    cin >> n;
#else
    int n = 1;
#endif
    for (int i = 0; i < n; ++i)
    {
        Solution(i + 1).solve();
    }
    return 0;
}