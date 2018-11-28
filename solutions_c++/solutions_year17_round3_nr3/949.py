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
        double u;
        cin >> u;
        vector<double> v(n);
        for (int i = 0; i < n; ++i)
        {
            cin >> v[i];
        }
        std::sort(v.begin(), v.end());
        while (u > 0.0)
        {
            bool is = false;
            for (int i = 1; i < n; ++i)
            {
                if (v[i] > v[0])
                {
                    double diff = min(u, v[i] - v[0]);
                    if (diff < 1e-12)
                        continue;
                    int m = i;
                    is = true;
                    for (int j = 0; j < i; ++j)
                    {
                        v[j] += diff / m;
                    }
                    u -= diff;
                    break;
                }
            }
            if (!is)
                break;
        }
        double ans = 1.0;
        for (int i = 0; i < n; ++i)
        {
            double add = min(u / n, 1.0 - v[i]);
            v[i] += add;
            ans *= v[i];
        }
        print();
        printf("%.9f\n", ans);
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