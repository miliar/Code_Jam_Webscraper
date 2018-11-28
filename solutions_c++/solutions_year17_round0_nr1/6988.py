#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int ss[s.size() - 1];
        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == '+') ss[i] = 1;
            else ss[i] = 0;
        }
        int kol = 0;
        for (int i = 0; i < s.size() - k + 1; ++i)
        {
            if (ss[i] == 0)
            {
                //for (int _ = 0; _ < s.size(); ++_) cout << ss[_];
                //cout << endl;
                ++kol;
                for (int j = i; j < i + k; ++j)
                    ss[j] = 1 - ss[j];
            }
        }
        bool flag = false;
        for (int i = s.size() - k + 1; i < s.size(); ++i)
        {
            if (ss[i] == 0)
            {
                flag = true;
                break;
            }
        }
        if (flag)
        {
            //for (int _ = 0; _ < s.size(); ++_) cout << ss[_];
            //cout << endl << s.size() - k + 1 << endl;
            cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
        }
        else
        {
            cout << "Case #" << i + 1 << ": " << kol << endl;
        }
    }
}
