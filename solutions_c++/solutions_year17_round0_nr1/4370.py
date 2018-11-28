#include <bits/stdc++.h>

using namespace std;

string s;
int n, k;
int solve()
{
    int ans = 0;
    for (int i = 0; i <= n - k; ++ i)
    {
        if (s[i] == '+') continue;
        for (int j = i; j < i + k; ++ j)
            if (s[j] == '+') s[j] = '-';
            else s[j] = '+';
        ++ ans;
    }
    for (int i = 0; i < n; ++ i)
        if (s[i] == '-')
            return -1;
    return ans;
}
void write(int x)
{
    if (x == -1) cout << "IMPOSSIBLE";
    else cout << x;
    cout << endl;
}

int main()
{
    freopen("lol.in", "r", stdin),
    freopen("output.out", "w", stdout);

    int t; cin >> t;
    for (int i = 1; i <= t; ++ i)
    {
        cin >> s >> k; n = s.size();
        cout << "Case #" << i << ": ";
        write(solve());
    }
}
