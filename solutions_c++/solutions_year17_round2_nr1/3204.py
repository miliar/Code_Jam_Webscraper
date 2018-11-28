#include <bits/stdc++.h>

#define LL long long
#define ii pair<int, int>
#define ff first
#define ss second

using namespace std;

void _solve() {
    int d, n;
    scanf("%d %d", &d, &n);

    vector<ii> data(n);
    for(int i = 0; i < n; i++) {
        scanf("%d %d", &data[i].ff, &data[i].ss);
    }

    long double res = 2e18, cur = 0;
    sort(data.begin(), data.end());
    int mi = n - 1; double miVal = -1;

    for(int i = 0; i < n; i++) {
        // miVal = max(miVal, (d - data[i].ff) / data[i].ss);
        // printf("%.6lf\n", (double) (d - data[i].ff) / data[i].ss);
        double val = (double) (d - data[i].ff) / data[i].ss;
        if(val > miVal) {
            miVal = val;
            mi = i;
        }

        // double d = data[i + 1].ss * ((data[i + 1].ff - data[i].ff) / (data[i].ss - data[i + 1].ss));
        // res = min(res, (d - cur) / ((d - data[n - 1].ff) / data[n - 1].ss));
    }



    printf("%.6lf\n", d / miVal);

    for(int i = 0; i < n; i++) {
        // printf("%d %d\n", data[i].ff, data[i].ss);
    }
}

int main() {
    int t;
    scanf("%d", &t);

    for(int tt = 1; tt <= t; tt++) {
        printf("Case #%d: ", tt);
        _solve();
    }

    return 0;
}