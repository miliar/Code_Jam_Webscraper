#include <bits/stdc++.h>
using namespace std;

void f(int ti)
{
    int n, k, vi, ls = -1, rs = -1;
    cin >> n >> k;
    vector<bool> a(n + 2);
    a[0] = a[n + 1] = true;
    for (int ki = 0; ki < k; ki++) {
        vi = ls = rs = -1;
        for (int i = 1; i <= n; i++) {
            if (a[i])
                continue;
            int cl = 0, cr = 0;
            for (int j = i - 1; !a[j]; j--, cl++);
            for (int j = i + 1; !a[j]; j++, cr++);
            if (min(cl, cr) > min(ls, rs) || (min(cl, cr) == min(ls, rs) && max(cl, cr) > max(ls, rs)))
                vi = i, ls = cl, rs = cr;
        }
        a[vi] = true;
    }
    cout << "Case #" << ti << ": " << max(ls, rs) << " " << min(ls, rs) << '\n';
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
        f(i);
}
