#include <bits/stdc++.h>
using namespace std;

using vs = vector<string>;

void f(vs& v, int s, int e, int k, int diff, int fl)
{
    for(int i = s, prev = s; i >= min(s, e) && i <= max(s, e); i += diff)
    {
        if(fl)
        {
            if(v[k][i] == '?') v[k][i] = v[k][prev];
        }
        else
        {
            if(v[i][k] == '?') v[i][k] = v[prev][k];
        }

        prev = i;
    }
}

void solve(int t)
{
    int R, C; cin >> R >> C;

    vs v(R);

    for(int i = 0; i < R; i++) cin >> v[i];

    for(int i = 0; i < R; i++)
    {
        f(v, 0, C - 1, i,  1, 1);
        f(v, C - 1, 0, i, -1, 1);
    }

    for(int i = 0; i < C; i++)
    {
        f(v, 0, R - 1, i,  1, 0);
        f(v, R - 1, 0, i, -1, 0);
    }

    cout << "Case #" << t << ":\n";
    for(auto& e : v) cout << e << '\n';
}

int main()
{
    ios_base::sync_with_stdio(0);

    int t; cin >> t;

    for(int i = 1; i <= t; i++) solve(i);

    return 0;
}
