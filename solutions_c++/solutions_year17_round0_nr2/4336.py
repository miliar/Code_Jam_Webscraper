#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

string solve(string s)
{
    for (int i = 1; i < s.size(); ++ i)
    {
        if (s[i] == '0' && s[i - 1] == '1')
        {
            return string(s.size() - 1, '9');
        }
        if (s[i] < s[i - 1])
        {
            int j = i - 2;
            while (j >= 0 && s[j] == s[i - 1]) -- j;
            -- s[++ j];

            for (++ j; j < s.size(); ++ j)
                s[j] = '9';
            return s;
        }
    }
    return s;
}

int main()
{
    freopen("lol.in", "r", stdin),
    freopen("output.out", "w", stdout);

    int t; cin >> t;
    for (int i = 1; i <= t; ++ i)
    {
        string s; cin >> s;
        cout << "Case #" << i << ": " << solve(s) << endl;
    }
}
