#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int n, d, T;
struct horse {
    int k, s;
} h[1010];
double t[1010];

bool operator < (const horse &a, const horse &b) {
    return (a.k < b.k) || (a.k == b.k && a.s > b.s);
}

int main(){
    cin >> T;
    for (int id = 1; id <= T; id++) {
        cin >> d >> n;
        for (int i = 0; i < n; ++i) cin >> h[i].k >> h[i].s;
        printf("Case #%d: ", id);

        sort(h, h + n);
        for (int i = 0; i < n; ++i) {
            t[i] = 1. * (d - h[i].k) / h[i].s;
            if (i < n - 1) {
                int ds = (h[i].s - h[i + 1].s);
                if (ds > 0) {
                    double nt = (h[i + 1].k - h[i].k) / ds;
                    t[i] = min(t[i], nt);
                }
            }
        }

        double ans = 1e100;
        for (int i = 0; i < n; i++) {
            double p = h[i].k + h[i].s * t[i];
            ans = min(ans, p / t[i]);
        }
        printf("%.8f\n", ans);
    }
}
