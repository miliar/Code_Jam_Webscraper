#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

double eps = 1e-10;
int Fabs(double x) {return (x > eps) - (x < -eps);}

struct Node {
    double k, s;
    bool operator < (const Node &_p) const {
        return k < _p.k;
    }
} p[1005];

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++) {
        double d;
        int n;
        cin >> d >> n;
        for(int i = 0; i < n; i ++) {
            cin >> p[i].k >> p[i].s;
        }
        sort(p, p + n);
        if(n == 1 || n == 2 && p[0].s <= p[1].s) {
            printf("Case #%d: %.7f\n", kase, d / ((d - p[0].k) / p[0].s));
        } else {
            double t1 = (d - p[0].k) / p[0].s;
            double t2 = (p[1].k - p[0].k) / (p[0].s - p[1].s);

            if(t2 < t1) {
                printf("Case #%d: %.7f\n", kase, d / ((d - p[1].k) / p[1].s));
            } else {
                printf("Case #%d: %.7f\n", kase, d / ((d - p[0].k) / p[0].s));
            }
        }
    }
    return 0;
}
