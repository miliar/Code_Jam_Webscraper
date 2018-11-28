#include <iostream>
#include <string>
using namespace std;

void solve()
{
    string s;
    int k;
    cin >> s >> k;
    int cnt = 0;
    for (int i = 0; i <= s.length() - k; ++i)
    {
        if (s[i] == '+')
            continue;
        ++cnt;
        for (int j = i; j < i + k; ++j)
        {
            if (s[j] == '+')
                s[j] = '-';
            else
                s[j] = '+';
        }
    }
    for (int i = s.length() - k + 1; i < s.length(); ++i)
    {
        if (s[i] == '-')
        {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << cnt << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) 
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
