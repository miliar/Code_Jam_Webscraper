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
    void print(int test, int ans)
    {
        if (ans == -1)
            cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << test << ": " << ans << endl;
    }

    void apply(vector<int>& v, int l, int r)
    {
        for (int i = l; i < r; ++i)
        {
            v[i] = !v[i];
        }
    }

    void solve(int test)
    {
        string str;
        int k;
        cin >> str >> k;
        vector<int> v(str.size());
        for (int i = 0; i < str.size(); ++i)
        {
            v[i] = str[i] == '+';
        }
        int ans = 0;
        for (int i = 0; i < v.size() - k; ++i)
        {
            if (!v[i])
            {
                ++ans;
                apply(v, i, i + k);
            }
        }

        set<int> q;
        for (int i = v.size() - k; i < v.size(); ++i)
        {
            q.insert(v[i]);
        }

        if (q.size() > 1)
        {
            print(test, -1);
        }
        else
        {
            if (*q.begin() == 0)
                ++ans;
            print(test, ans);
        }
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