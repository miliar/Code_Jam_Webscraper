#include <bits/stdc++.h>
using namespace std;
const int M = 1e5+10;

int n;
double D, k[M], s[M];

int main() {
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int t; scanf("%d", &t);
    int Cas = 0;
    while(t --) {
        scanf("%lf%d", &D, &n);
        double mx = 0;
        for(int i = 0; i < n; i ++) {
            scanf("%lf%lf", &k[i], &s[i]);    
            mx = max(mx, (D-k[i])/s[i]);
        }
        printf("Case #%d: %.6f\n", ++Cas, D/mx);
    }
}
