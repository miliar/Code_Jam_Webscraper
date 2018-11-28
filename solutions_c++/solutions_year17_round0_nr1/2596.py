#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
typedef unsigned long long ull;
using namespace std;

void imp(int t)
{
    cout << "Case #" << t  << ": IMPOSSIBLE" << endl;
}

void solve(string s, int k, int t)
{
    if (s.length() < k)
    {
        imp(t);
        return;
    }
    int ans = 0;
    for (int p = 0; p <= s.size() - k; ++p)
    {
        if (s[p] == '-')
        {
            ++ans;
            for (int j = p; j < p + k; ++j)
                if (s[j] == '+')
                    s[j] = '-';
                else
                    s[j] = '+';
        }
    }
    for (int p = s.size() - k + 1; p < s.size(); ++p)
    {
        if (s[p] == '-')
        {
            imp(t);
            return;
        }
    }
    cout << "Case #" << t << ": " << ans << endl;
}

int main()
{
    int k, t;
    string s;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cin >> s >> k;   
        solve(s, k, i + 1);
    }
}
