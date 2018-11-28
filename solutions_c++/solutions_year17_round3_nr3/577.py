#include <bits/stdc++.h>

typedef long long ll;

double EPS = 1e-7;

using namespace std;

int main() {

    // freopen("C-small-1-attempt1.in", "r", stdin);
    // freopen("C-small-1-attempt1.out", "w", stdout);

    int T, k = 0, N, K, i, j, l; double p[50], u, a, r;

    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++k);
        scanf("%d%d%lf", &N, &K, &u);
        for(i=0;i<N;i++)
            scanf("%lf", &p[i]);
        sort(p, p+N);
        for(i=0;i<N&&u>EPS;) {
            for(j=i+1;j<N&&fabs(p[i]-p[j])<EPS;j++);
            a = u / j;
            if (j < N)
                a = min(fabs(p[j] - p[i]), a);
            u -= a * j;
            for(l=0;l<j;l++)
                p[l] += a;
            if (j == N) break;
            i = j;
        }
        r = 1.0;
        for(i=0;i<N;i++)
            r *= min(1.0, p[i]);
        printf("%.8f\n", r);
    }

    return 0;
}
