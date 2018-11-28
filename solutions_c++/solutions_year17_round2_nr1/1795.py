#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("/Inputs/GC2017/in.txt", "r", stdin);
    freopen("/Inputs/GC2017/out.txt", "w", stdout);
    
    int t;
    scanf("%d", &t);
    
    for (int c = 1; c <= t; c++) {
        double d, n;
        scanf("%lf%lf", &d, &n);
        vector<pair<int, int>> h(n);
        double mxspd = INT_MAX;
        for (int i = 0; i < n; i++) {
            double s, p;
            scanf("%lf%lf", &p, &s);
            h[i] = {s, p};
            mxspd = min(mxspd, d / ((d - p) / s));
        }
        printf("Case #%d: %lf\n", c, mxspd);
    }
    
    return 0;
}
