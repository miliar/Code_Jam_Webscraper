#include <bits/stdc++.h>
using namespace std;

#ifndef LOCAL
#define endl "\n"
#endif

#define mp(a, b) make_pair(a, b)
#define forn(i, n) for (int i = 0; i < n; ++i)
#define form(i, n, m) for (int i = n; i < m; ++i)
#define pb push_back

void inv(char& a)
{
    if (a == '-') a = '+';
    else a = '-';
}

signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int test_count;
    cin >> test_count;
    for (int test_num = 1; test_num <= test_count; ++test_num)
    {
        string s;
        int k;
        cin >> s >> k;
        int ind = 0, res = 0;
        while (ind < (int)s.size())
        {
            while (ind < (int)s.size() && s[ind] == '+') ++ind;
            if (ind + k > (int)s.size())
            {
                break;
            }
            for (int i = ind; i < ind + k; ++i)
            {
                inv(s[i]);
            }
            ++res;
        }
        cout << "Case #" << test_num << ": ";
        if (ind != (int)s.size())
        {
            cout << "IMPOSSIBLE";
        }
        else
        {
            cout << res;
        }
        cout << endl;
    }
    return 0;
}

