#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;

double P[55];

#define D
#define EPS 1e-6

int main() {
    int T;
    scanf("%i", &T);
    for (int t = 0; t < T; t++) {
        int N, K;
        scanf("%i %i", &N, &K);
        assert(N == K);
        double U;
        scanf("%lf", &U);
        for (int i = 0; i < N; i++) {
            scanf("%lf", &P[i]);
        }

        if (N == 1) {
            P[0] += U;
            printf("Case #%i: %lf\n", t+1, P[0]);
        } else {
            P[N++] = 1.0;
            while (U > EPS) {
                std::sort(P, P+N, std::less<double>());
                for (int i = 0; i < N; i++)  D("%lf ", P[i]);
                D("\n");
                int i = 0;
                int e = i+1;
                while (e < N) {
                    if (std::abs(P[i] - P[e]) > EPS)  break;
                    e++;
                }
                int cnt = e - i;
                double by = std::max(0.0, std::min((P[e] - P[i])*cnt, U));
                if (by < EPS)  break;
                D("(U=%lf) Adding %lf to %lf(%i...end%i)\n", U, by, P[i], i, e);
                for (int j = i; j < e; j++) {
                    P[j] += by / cnt;
                }
                U -= by;
            }
            double ans = 1;
            for (int i = 0; i < N; i++)   ans *= P[i];
            printf("Case #%i: %lf\n", t+1, ans);
        }
    }
}
