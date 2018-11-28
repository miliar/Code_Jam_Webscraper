#include <bits/stdc++.h>
#define all(a) (a).begin(),(a).end()
#define mp make_pair
#define pb push_back
using namespace std;

const int N = 1e3 + 5;

int t, n, a[6], b[N], first;
string s;
bool good = 0;

void rec(int pos, int x)
{
    if (good) return;
    if ((a[0] + a[2]) + 1 < a[4]) return;
    if ((a[0] + a[4]) + 1 < a[2]) return;
    if ((a[4] + a[2]) + 1 < a[0]) return;
    b[pos] = x;
    --a[x];
    if (pos == n - 1)
    {
        if (x == first)
        {
            ++a[x];
            return;
        }
        for (int i = 0; i < n; ++i)
        {
            if (b[i] == 0) s.push_back('R');
            if (b[i] == 2) s.push_back('Y');
            if (b[i] == 4) s.push_back('B');
        }
        good = 1;
        ++a[x];
        return;
    }
    for (int i = 0; i < 5; i += 2)
        if (a[i] && i != x) rec(pos + 1, i);
    ++a[x];
}


//bool q = 0;
void solve()
{
    cin >> n;
    for (int i = 0; i < 6; ++i)
        cin >> a[i];
    if (q) return;
    s.clear();
    first = -1;
    good = 0;
    for (int i = 0; i < 5 && !good; i += 2)
        if (a[i]) first = i, rec(0, i);
    if (s.empty()) cout << "IMPOSSIBLE";
    else cout << s;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("1.out","w",stdout);
   // ios_base::sync_with_stdio(0);
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
       // q = (i==36);
        cout << "Case #" << i << ": ";
        solve();
        cout << "\n";
    }
}
