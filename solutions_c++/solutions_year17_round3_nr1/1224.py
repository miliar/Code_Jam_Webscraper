#include <bits/stdc++.h>
using namespace std;

const int kN = 1e3 + 10;
pair<int64_t, int64_t> P[kN];

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T, t = 1;
    cin >> T;
    while (t <= T) {
        int N, K;
        cin >> N >> K;
        for (int i = 0; i < N; ++i) cin >> P[i].first >> P[i].second;
        auto Comp = [](pair<int64_t, int64_t>& p1, pair<int64_t, int64_t>& p2) {
            return p1.first * p1.second > p2.first * p2.second;
        };
        sort(P, P + N, Comp);
        int64_t mx = 0;
        for (int i = 0; i < N; ++i) {
            int64_t sm = P[i].first * P[i].first;
            if (i < K) {
                for (int j = 0; j < K; ++j) sm += 2 * P[j].first * P[j].second;
            } else {
                for (int j = 0; j + 1 < K; ++j) sm += 2 * P[j].first * P[j].second;
                sm += 2 * P[i].first * P[i].second;
            }
            mx = max(mx, sm);
            //cout << i << " " << P[i].first << " " << P[i].second << " " << sm << " " << mx << endl;
        }
        cout << "Case #" << t++ << ": ";
        cout << fixed << setprecision(9) << 1.0 * M_PI * mx << "\n";
    }
    return 0;
}
