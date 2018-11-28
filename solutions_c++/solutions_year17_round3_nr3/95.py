#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
using namespace std;
#define EPS 1e-8
#define MAXN 52
int N, K;
double u, p[MAXN];
int main()
{
    int T;
    cin >> T;
    for (int Ti = 1; Ti <= T; ++Ti) {
        cin >> N >> K;
        cin >> u;
        for (int i = 0; i < N; ++i)
            cin >> p[i];
        sort(p, p + N);
        p[N] = 1;
        while (fabs(u) > EPS) {
            int m = 1;
            while (m < N && fabs(p[0] - p[m]) < EPS)
                ++m;
            double d = min(u, m * (p[m] - p[0]));
            double di = d / m;
            for (int i = 0; i < m; ++i)
                p[i] += di;
            u -= d;
        }
        double ans = 1;
        for (int i = 0; i < N; ++i)
            ans *= p[i];
        printf("Case #%d: %.10lf\n", Ti, ans);
    }
    return 0;
}
