#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int main()
{
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        double d; int n;
        scanf("%lf %d\n", &d, &n);

        double a,b;
        vector<pair<double, double > > v;
        for (int i = 0; i < n; i++) {
            scanf("%lf %lf", &a, &b);
            v.push_back({a,b});
        }
        sort(v.rbegin(), v.rend());

        double time = 0;
        for (auto p : v) {
            time = max(time, (d - p.first)/p.second);
        }

        printf("Case #%d: %lf\n", t, d/time);
    }
}
