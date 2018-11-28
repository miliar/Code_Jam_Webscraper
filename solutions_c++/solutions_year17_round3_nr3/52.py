#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
typedef long long ll;

int T;

int main() {
    scanf("%d", &T);
    fo(_,1,T+1) {
        printf("Case #%d: ", _);

        int n, k; double u, p[55];
        scanf("%d %d %lf", &n, &k, &u);
        fo(i,0,n) scanf("%lf", p+i);
        double mn = 0, mx  = 1, md;
        fo(j,0,300) {
            md = (mn+mx)/2;
            double cst = 0;
            fo(i,0,n) cst += max(0., md - p[i]);
            if (cst - 1e-10 > u) mx = md;
            else mn = md;
        }
        //printf("%lf\n", md);

        double ans = 1;
        fo(i,0,n) ans *= max(p[i], mn);
        printf("%.9lf\n", ans);
    }

    return 0;
}
