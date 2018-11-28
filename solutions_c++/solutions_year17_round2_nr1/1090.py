#define DEBUG
#define TXTOUT
#include<bits/stdc++.h>
using namespace std;
const double PI = acos(-1.0);
const double EPS = 1e-8;
const int M = 1e3 + 10;
int d, n;
int k[M], s[M];
double Solve() {
    double answer = 0;
    for (int i = 0; i < n; i++) {
        double t = (d - k[i]) * 1.0 / s[i];
        if (i == 0) {
            answer = d / t;
            continue;
        }
        answer = min(answer, d / t);
    }
    return answer;
}
int main() {
    #ifdef TXTOUT
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    #endif // TXTOUT
    int t, cas = 1;
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d", &d, &n);
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &k[i], &s[i]);
        }
        printf("Case #%d: %.6f\n", cas++, Solve());
    }
    return 0;
}
