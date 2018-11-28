#include <bits/stdc++.h>

using namespace std;

void solve(int tst)
{
    cout << "Case #" << tst << ": ";
    string s;
    cin >> s;
    int f = -1;
    for (int i = 1; i < s.size(); ++i) {
        if (s[i] - '0' < s[i - 1] - '0') {
            f = i - 1;
            break;
        }
    }
    if (f == -1) {
        cout << s << endl;
        return;
    }
    for (int i = f; i >= 0; --i) {
        int cur = s[i];
        if (s[i] != '0' && (i == 0 || s[i] - '0' - 1 >= s[i - 1] - '0')) {
            --s[i];
            for (int j = i + 1; j < s.size(); ++j) {
                s[j] = '9';
            }
            break;
        }
    }
    int p = 0;
    if (s[0] == '0') {
        ++p;
    }
    for (; p < s.size(); ++p) {
        cout << s[p];
    }
    cout << endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        solve(i);
    }
}
