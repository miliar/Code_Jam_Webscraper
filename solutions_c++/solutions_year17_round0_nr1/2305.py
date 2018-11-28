#include <bits/stdc++.h>
using namespace std;

void solve(int t)
{
    string s; cin >> s;
    int k; cin >> k;

    int n = s.size();

    int ans = 0;

    for(int i = 0; i < n; i++) if(s[i] == '-')
    {
        if(i > n - k)
        {
            cout << "Case #" << t << ": IMPOSSIBLE" << '\n';
            return;
        }

        for(int j = 0; j < k; j++)
        {
            auto& c = s[i + j];

            c = c == '+' ? '-' : '+';
        }

        ans++;
    }

    cout << "Case #" << t << ": " << ans << '\n';
}

int main()
{
    ios_base::sync_with_stdio(0);

    int T; cin >> T;

    for(int t = 1; t <= T; t++) solve(t);

    return 0;
}
