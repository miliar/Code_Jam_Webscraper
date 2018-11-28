#include "bits/stdc++.h"
using namespace std;
const int N = 1e5 + 5;
const int LGN = 21;
int tt;
int d , n;
int K[N];
int S[N];

bool ok(double x) {
    double tm = (double) (1.0 * d) / x;
    for(int i = 1; i <= n; ++i) {
        double cur = (double) (1.0 * (d - K[i]) ) / (double) (1.0 * S[i]);
        if(cur > tm) {
            return 0;
        }
    }
    return 1;
}


double solve() {
    double rekt = 0.0;
    for(int i = 1; i <= n; ++i) {
        double cur = (double) (1.0 * (d - K[i] ) ) / (double) (1.0 * S[i]);
        rekt = max(rekt , cur);
    }
    return (double) (1.0 * d) / rekt;
}

int main() {
    freopen("QLinput.txt" , "r" , stdin);
    freopen("QLoutput.txt" , "w" , stdout);
    scanf("%d" , &tt);
    for(int TT = 1; TT <= tt; ++TT) {
        printf("Case #%d: " , TT);
        scanf("%d %d" , &d , &n);
        for(int i = 1; i <= n; ++i) {
            scanf("%d %d" , K + i , S + i);
        }
        double ans = solve();
        printf("%.7f\n" , ans);
    }
    return 0;
}
