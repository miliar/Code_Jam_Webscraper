#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int N = 1e6 + 10;

struct ly
{
    int mn, mx, idx;
    ly(int f1, int f2, int f3)
    {
        mn = f1, mx = f2, idx = f3;
    }
};
bool operator<(const ly& f, const ly& s)
{
    if (f.mn != s.mn) return f.mn < s.mn;
    if (f.mx != s.mx) return f.mx < s.mx;
    return f.idx > s.idx;
}
char us[N];
void solve()
{
    for (int i = 0; i < N; ++ i)
        us[i] = false;
    int n, k; cin >> n >> k; n += 2;
    us[0] = us[n - 1] = true;

    priority_queue <ly> q;
    {
        int tl = 0, tr = n - 1, idx;
        idx = (tl + tr) >> 1;
        q.push(ly(idx - tl, tr - idx, idx));
    }

    int c = 0;
    while (q.size())
    {
        int tl, tr, idx, mn, mx;
        {
            ly cur = q.top();
            q.pop();

            mn = cur.mn, mx = cur.mx, idx = cur.idx;
            tl = idx - mn, tr = idx + mx;
            if (tl == tr) continue;
        }
        if (us[idx]) continue;
        us[idx] = true;
        ++ c;
        if (c == k)
        {
            cout << mx - 1 << " " << mn - 1 << endl;
            return;
        }

        int tm = (tl + idx) >> 1;
        q.push(ly(tm - tl, idx - tm, tm));
        tm = (tr + idx) >> 1;
        q.push(ly(tm - idx, tr - tm, tm));
    }

}

int main()
{
    freopen("input.in", "r", stdin),
    freopen("output.txt", "w", stdout);

    int t; cin >> t;
    for (int i = 1; i <= t; ++ i)
    {
        cout << "Case #" << i << ": ";
        solve();
    }
}
