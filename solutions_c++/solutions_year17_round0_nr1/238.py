#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int N = 1e3 + 10;

int solve() {
    string s;
    cin >> s;
    int k, n = s.size();
    cin >> k;
    int res = 0;
    for (int i = 0; i < n - k + 1; i++) {
        if (s[i] == '-') {
            for (int j = i; j < i + k; j++)
                s[j] = (s[j] == '+' ? '-' : '+');
            res++;
        }
    }
    for (int i = n - k + 1; i < n; i++)
        if (s[i] == '-')
            return -1;
    return res;
}

int main()
{
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int res = solve();
        cout << "Case #" << i << ": ";
        if (res < 0)
            cout << "IMPOSSIBLE\n";
        else
            cout << res << "\n";
    }
    cin.tie(nullptr);
    return 0;
}
