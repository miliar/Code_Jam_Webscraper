#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        int D, n;
        scanf("%d%d", &D, &n);
        long long kk, vv;
        for (int i = 1; i <= n; i++) {
            int k, v;
            scanf("%d%d", &k, &v);
            /*
            if (i == 1 || kk/vv < (D-k)/v) {
                
            }*/
            if (i == 1 || (kk * v < vv * (D-k))) {
                kk = D-k;
                vv = v;
            }
            /*
            double tmp = 1.0*(D-k)/v;
            if (tmp > tt) {
                kk = k, vv = v;
            }*/
        }
        double ans = 1.0*D * vv / kk;
        printf("Case #%d: %.10f\n", ++cas, ans);
    }
}