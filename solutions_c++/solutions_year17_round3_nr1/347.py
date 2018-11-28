#include <bits/stdc++.h>
using namespace std;

double M_PI = atan(1) * 4;
pair<double, double> rh[1001];
double r[1001];
double h[1001];

bool in_memo[1001][1001];
double memo[1001][1001];

double opt(int i, int k) {
    if(!in_memo[i][k]) {
        if(i == 0 || k == 0) {
            memo[i][k] = 0;
        } else {
            memo[i][k] = max(
                opt(i-1, k-1) + 2 * M_PI * r[i] * h[i],
                opt(i-1, k)
            );
        }
        in_memo[i][k] = true;
    }
    return memo[i][k];
}

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int N, K;
        cin >> N >> K;
        for(int i = 1; i <= N; i++) {
            double R, H;
            cin >> R >> H;
            rh[i] = {R, H};
        }
        sort(rh + 1, rh + 1 + N);
        for(int i = 1; i <= N; i++) {
            r[i] = rh[i].first;
            h[i] = rh[i].second;
        }
        memset(in_memo, false, sizeof in_memo);
        double ans = M_PI * r[K] * r[K] + 2 * M_PI * r[K] * h[K] + opt(K - 1, K - 1);
        for(int i = K + 1; i <= N; i++) {
            ans = max(ans, M_PI * r[i] * r[i] + 2 * M_PI * r[i] * h[i] + opt(i - 1, K - 1));
        }
        cout << "Case #" << t << ": " << fixed << setprecision(7) << ans << endl;
    }
    return 0;
}
