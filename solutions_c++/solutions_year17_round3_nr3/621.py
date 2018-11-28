#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn = 110;
double p[maxn];

int main() {
    int T;
    cin >> T;
    for (int ca = 1; ca <= T; ca++) {
        int N, K;
        cin >> N >> K;
        double U;
        cin >> U;
        for (int i = 1; i <= N; i++) cin >> p[i];
        sort(p + 1, p + N + 1);
        for (int i = 1; i <= N - 1; i++) {
            double d = p[i + 1] - p[i];
            if (d * i > U) {
                for (int j = 1; j <= i; j++) p[j] += U / i;
                U = 0;
                break;
            } else {
                for (int j = 1; j <= i; j++) p[j] = p[i + 1];
                U -= d * i;
            }
        }
        if (U > 0)
            for (int i = 1; i <= N; i++) p[i] += U / N;
        double ans = 1;
        for (int i = 1; i <= N; i++) ans *= p[i];
        printf("Case #%d: %.8lf\n", ca, ans);
    }
    return 0;
}