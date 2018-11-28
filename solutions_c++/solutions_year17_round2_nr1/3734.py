#include <iostream>
#include <bits/stdc++.h>

using namespace std;
using ll = long long;

const double eps = 1e-9;

struct Horse
{
    double k;
    int s;
    int i;
};

int main(int argc, char *argv[])
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int tc;
    cin >> tc;
    for (int t = 1; t <= tc; t++)
    {
        cout << "Case #" << t << ": ";
        int d, n;
        cin >> d >> n;
        Horse h[2000] = {};
        double time[2000] = {};
        for (int i = 0; i < n; i++)
        {
            cin >> h[i].k >> h[i].s;
        }
        sort(h, h + n, [](Horse h1, Horse h2) -> bool {return h1.k < h2.k;});
        for (int i = 0; i < n; i++)
        {
            h[i].i = i;
            time[i] = 0;
        }
        h[n] = {d, 0, n};
        double tt = 0;
        while ((d - h[0].k) > eps)
        {
            int ind = -1;
            double tmin = INT_MAX;
            for (int i = 0; i < n; i++)
            {
                if (h[i].s <= h[i + 1].s)
                    continue;
                double tcur = (h[i + 1].k - h[i].k) / (h[i].s - h[i + 1].s);
                if (tcur < tmin)
                {
                    tmin = tcur;
                    ind = i;
                }
            }
            if (ind == -1)
                break;
            for (int i = n - 1; i >= 0; i--)
            {
                h[i].k += h[i].s * tmin;
                if (h[i + 1].k - h[i].k < eps)
                {
                    h[i].s = h[i + 1].s;
                }
            }
            tt += tmin;
        }
        if (h[0].s > 0)
            tt += (d - h[0].k) / h[0].s;
        cout << setprecision(20) << (1.0 * d / tt) << '\n';
    }
    return 0;
}
