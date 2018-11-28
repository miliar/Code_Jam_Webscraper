#include <bits/stdc++.h>
using namespace std;

int t, pos;
string s;
char c;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie();
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    cin >> t;
    for (int ii = 0; ii < t; ++ii)
    {
        cin >> s;
        if ((int)s.size() == 1)
        {
            cout << "Case #" << ii + 1 << ": " << s << "\n";
            continue;
        }
        c = s[0];
        pos = 0;
        for (int i = 1; i < (int)s.size(); ++i)
        {
            if (s[i - 1] != c)
            {
                pos = i - 1;
                c = s[i - 1];
            }
            if (s[i] < s[i - 1])
            {
                s[pos] = (char)(s[pos] - 1);
                for (int j = pos + 1; j <= (int)s.size(); ++j)
                    s[j] = '9';
                break;
            }
        }
        while (s[0] == '0') s.erase(0, 1);
        cout << "Case #" << ii + 1 << ": " << s << "\n";
    }
}
