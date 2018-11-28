#include <cstdio>
#include <algorithm>
using namespace std;

int N, K;
double U, p[50], q[50];

double solve() {
    scanf("%d%d%lf", &N, &K, &U);
    for (int i = 0; i < N; i++)
        scanf("%lf", p + i);
    sort(p, p + N);
    q[0] = p[0];
    for (int i = 1; i < N; i++)
        q[i] = p[i] + q[i - 1];
    for (int i = 0; i < N; i++) {
        if (i == N - 1 || (q[i] + U) / (i + 1) <= p[i + 1]) {
            double ans = 1;
            double k = (q[i] + U) / (i + 1);
            for (int j = 0; j <= i; j++)
                ans *= k;
            for (int j = i + 1; j < N; j++)
                ans *= p[j];
            return ans;
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++)
        printf("Case #%d: %.9lf\n", i, solve());
}
