#include <iostream>
#include <string>
using namespace std;

void solve()
{
    long long n;
    cin >> n;
    string s = to_string(n);
    for (int i = s.length() - 1; i > 0; --i)
    {
        if (s[i - 1] > s[i])
        {
            for (int j = i; j < s.length(); ++j)
                s[j] = '9';
            --s[i - 1];
        }
    }
    long long res = 0;
    for (int i = 0; i < s.length(); ++i)
        res = res * 10 + s[i] - '0';

    cout << res << endl;
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
    return 0;
}
