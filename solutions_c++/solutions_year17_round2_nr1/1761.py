#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int main() {
//    freopen("A-small-attempt0.in", "r", stdin);
//    freopen("A-small-attempt0.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    int D, N;
    int Ki, Si;

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &D, &N);
        vector<pair<int, int>> KS;
        for (int j = 0; j < N; j++) {
            scanf("%d %d", &Ki, &Si);
            KS.push_back({Ki, Si});
        }
        sort(KS.begin(), KS.end());
        double mint = 0;
        for (auto &p : KS) {
            mint = max(mint, (D - p.first) / (double)p.second);
        }
        printf("Case #%d: %.7lf\n", t, D / mint);
    }

    return 0;
}

