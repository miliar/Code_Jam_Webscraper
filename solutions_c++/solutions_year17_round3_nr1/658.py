#include <cstdio>
#include <algorithm>
#include <set>
#include <queue>

std::pair<int, int> n[1007];
std::priority_queue<long double> S;

long double pole(long double r) {
    return r * r;
}

long double p(long double r, long double h) {
    return r * h;
}

int main() {
    int T;
    scanf("%d", &T);
    int N, K;
    for (int t = 1; t <= T; t++) {
        scanf("%d%d", &N, &K);
        for (int i = 0; i < N; i++) {
            scanf("%d%d", &n[i].first, &n[i].second);
        }
        std::sort(n, n + N);
        while (!S.empty())
            S.pop();
        long double sum = 0;
        long double wyn = 0;
        for (int i = 0; i < N; i++) {
            long double mp = p(n[i].first, n[i].second);
            if (i >= K - 1) {
                wyn = std::max(wyn, (sum + mp) * 2.0 + pole(n[i].first));
            }
            if (i < K - 1) {
                S.push(-mp);
                sum += mp;
            } else {
                if (!S.empty()) {
                    if (-S.top() < mp) {
                        sum -= -S.top();
                        sum += mp;
                        S.pop();
                        S.push(-mp);
                    }
                }
            }
        }
        printf("Case #%d: %Lf\n", t, wyn * M_PI);
    }
    return 0;
}