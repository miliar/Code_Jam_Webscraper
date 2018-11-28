#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        int d, n;
        scanf("%d %d", &d, &n);
        double mt = 0;
        FO(i,0,n) {
            int k, s;
            scanf("%d %d", &k, &s);
            double t = (d - k) / 1. / s;
            mt = max(mt, t);
        }
        printf("Case #%d: %.9lf\n", Z, d / mt);
    }
}

