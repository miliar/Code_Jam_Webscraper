#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int n, k;

struct st
{
    int l, r, fs, sc;
    st (int l, int r, int fs, int sc) : l(l), r(r), fs(fs), sc(sc) {}
    st () {}
};

bool operator < (st a, st b)
{
    if (a.fs != b.fs)
        return a.fs > b.fs;
    if (a.sc != b.sc)
        return a.sc > b.sc;
    return a.l < b.l;
}

int get_fs(int l, int r)
{
    return (l + r)/2 - l;
}

int get_sc(int l, int r)
{
    return r - (l + r)/2;
}

void solve(int x)
{
    set <st> s;
    cin >> n >> k;
    s.insert(st(1, n, get_fs(1, n), get_sc(1, n)));
    while (k > 1)
    {
        st u = *s.begin();
        int l = u.l, r = u.r;
        int mid = (l + r) / 2;
        s.erase(s.begin());
        if (mid > l)
            s.insert(st(l, mid - 1, get_fs(l, mid - 1), get_sc(l, mid - 1)));
        if (mid < r)
            s.insert(st(mid + 1, r, get_fs(mid + 1, r), get_sc(mid + 1, r)));
        k--;
    }
    st u = *s.begin();
    cout << "Case #" << x << ": ";
    cout << u.sc << ' ' << u.fs;
    cout << '\n';
}

int main()
{
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
        solve(i);
    return 0;
}
