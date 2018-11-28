#include <bits/stdc++.h>

using namespace std;

const double EPS = 1e-8;

int D, n, k[1005], s[1005];

int cmp(double a, double b) {
    if (fabs(a-b) < EPS) return 0;
    if (a-b < EPS) return -1;
    return 1;
}

bool ok(double M) {
    for (int i = 1; i <= n; ++i) {
        if (cmp(M,s[i]) <= 0) continue;
        double T = k[i]/(M-s[i]);
        double x = (double)D / T;
        if (cmp(M,x) < 0) return false;
    }
    return true;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int t; scanf("%d",&t); int te = t;
    while (t--) {
        scanf("%d%d",&D,&n);
        for (int i = 1; i <= n; ++i)
            scanf("%d%d",&k[i],&s[i]);
        double L = 0, R = 100000000000000.0, res = -1;
        for (int i = 0; i < 70; ++i) {
            double M = (L+R)/2.0;
            if (ok(M)) {
                res = M;
                L = M;
            }
            else R = M;
        }
        cout << "Case #" << te-t << ": ";
        cout << fixed << setprecision(6) << res << endl;
    }
	return 0;
}
