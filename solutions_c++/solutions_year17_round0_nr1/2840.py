#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int solve(string s, int k) {
    int n = s.size();
    int moves = 0;
    for (int i = 0; i + k <= n; ++i) {
        if (s[i] == '-') {
            ++moves;
            for (int j = 0; j < k; ++j)
                s[i + j] ^= 6;
        }
    }
    for (int i = 0; i < n; ++i)
        if (s[i] == '-')
            moves = (int)1e9;
    return moves;
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int ttt = 1; ttt <= T; ++ttt) {
        string s;
        int k;
        cin >> s >> k;
        int ans = solve(s, k);
        reverse(s.begin(), s.end());
        ans = min(ans, solve(s, k));
        if (ans < (int)1e9)
            cout << "Case #" << ttt << ": " << ans << "\n";
        else
            cout << "Case #" << ttt << ": IMPOSSIBLE\n";
    }

    return 0;
}
