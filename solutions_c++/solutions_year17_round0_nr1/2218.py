#include <bits/stdc++.h>

using namespace std;

void solve(int test_num)
{
    string s;
    int k;
    cin >> s >> k;
    int ans = 0;
    int n = s.size();
    for (int i = 0; i < n - k + 1; i++) {
        if (s[i] == '+') {
            continue;
        }
        ans++;
        for (int j = 0; j < k; j++) {
            if (s[i + j] == '+') {
                s[i + j] = '-';
            } else {
                s[i + j] = '+';
            }
        }
    }
    cout << "Case #" << test_num << ": ";
    for (int j = n - k + 1; j < n; j++) {
        if (s[j] != '+') {
            cout << "IMPOSSIBLE\n";
            return;
        }
    }
    cout << ans << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        solve(i);
    }
}
