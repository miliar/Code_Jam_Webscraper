#include <bits/stdc++.h>

using namespace std;

void solve(int tst)
{
    cout << "Case #" << tst << ": ";
    string s;
    int k;
    cin >> s >> k;
    int ans = 0;
    for (int i = k - 1; i < s.size(); ++i) {
        if (s[i - k + 1] == '-') {
            ++ans;
            for (int j = i - k + 1; j <= i; ++j) {
                if (s[j] == '-') {
                    s[j] = '+';
                } else {
                    s[j] = '-';
                }
            }
        }
    }
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '-') {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << ans << endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        solve(i);
    }
}
