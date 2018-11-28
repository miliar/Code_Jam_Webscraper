#include <bits/stdc++.h>

using namespace std;

typedef long long LL;



int main() {
//    freopen("A-small-attempt1.in", "r", stdin);
//    freopen("A-small-attempt1.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    int N, K;

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        vector<pair<double, int>> pans;
        unordered_set<int> Rs;
        scanf("%d %d", &N, &K);
        for (int i = 0; i < N; i++) {
            int R, H;
            scanf("%d %d", &R, &H);
            pans.push_back({M_PI * 2 * R * H, R});
            Rs.insert(R);
        }
        sort(pans.begin(), pans.end(), greater<pair<double, int>>());
        double res = 0;
        for (auto R : Rs) {
            int idx = -1;
            for (int i = 0; i < N; i++) {
                if (pans[i].second == R) {
                    if (idx == -1 || pans[i].first > pans[idx].first) idx = i;
                }
            }
            double sum = M_PI * R * R + pans[idx].first;
            res = max(res, sum);
            int cnt = 1;
            for (int i = 0; i < N; i++) {
                auto &p = pans[i];
                if (p.second <= R && i != idx) {
                    sum += p.first;
                    if (++cnt == K) {
                        res = max(res, sum);
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %.7lf\n", t, res);
    }

    return 0;
}

