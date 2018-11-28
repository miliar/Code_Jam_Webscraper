#include <bits/stdc++.h>
using namespace std;

using ld = long double;
using vd = vector<ld>;

ld pi = acosl(-1);

ld circle_area(ld r)
{
    return pi * r * r;
}

ld height_area(ld r, ld h)
{
    return ld(2) * pi * r * h;
}

void solve(int t)
{
    int n, k; cin >> n >> k;

    vd rv(n), hv(n);

    for(int i = 0; i < n; i++)
        cin >> rv[i] >> hv[i];

    ld ans = 0;

    for(int i = 0; i < n; i++)
    {
        ld ca = circle_area(rv[i]);
        ld sum_ha = height_area(rv[i], hv[i]);

        vd ha(n);

        for(int j = 0; j < n; j++)
        if(j != i && rv[j] <= rv[i])
        {
            ha[j] = height_area(rv[j], hv[j]);
        }

        sort(begin(ha), end(ha));

        for(int j = n - 1, q = 1; q < k; q++, j--)
            sum_ha += ha[j];

        ans = max(ans, ca + sum_ha);
    }

    cout << fixed << setprecision(9) << "Case #" << t << ": " << ans << endl;
}

int main()
{
    ios_base::sync_with_stdio(0);

    int t; cin >> t;

    for(int i = 1; i <= t; i++) solve(i);

    return 0;
}
