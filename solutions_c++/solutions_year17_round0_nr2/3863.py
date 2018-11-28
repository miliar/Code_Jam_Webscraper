#include <bits/stdc++.h>
using namespace std;

#ifndef LOCAL
#define endl "\n"
#endif

#define mp(a, b) make_pair(a, b)
#define forn(i, n) for (int i = 0; i < n; ++i)
#define form(i, n, m) for (int i = n; i < m; ++i)
#define pb push_back

signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int test_count;
    cin >> test_count;
    for (int test_num = 1; test_num <= test_count; ++test_num)
    {
        string n;
        cin >> n;
        int ind = 0;
        while (ind < (int)n.size() && n[ind] == '1') ++ind;
        while (ind < (int)n.size() && n[ind] == '0') ++ind;
        if (ind == (int)n.size() && n.back() == '0')
        {
            cout << "Case #" << test_num << ": ";
            for (int i = 0; i + 1 < (int)n.size(); ++i)
            {
                cout << '9';
            }
            cout << endl;
            continue;
        }
        string ans;
        for (int i = 0; i + 1 < (int)n.size(); ++i)
        {
            if (n[i + 1] < n[i])
            {
                while (ans.size() && ans.back() == n[i]) ans.pop_back();
                if ((int)ans.size() <= i)
                {
                    ans.push_back(n[i] - 1);
                }
                while (ans.size() + 1 < n.size())
                {
                    ans.push_back('9');
                }
                n.back() = '9';
                break;
            }
            else
            {
                ans.push_back(n[i]);
            }
        }
        ans.push_back(n.back());
        cout << "Case #" << test_num << ": ";
        ind = 0;
        while (ind < (int)ans.size() && ans[ind] == '0') ++ind;
        ind -= (ind == (int)ans.size());
        for (int i = ind; i < (int)ans.size(); ++i)
        {
            cout << ans[i];
        }
        cout << endl;
    }
    return 0;
}

