#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int main() {
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        int n, k;
        double t;
        scanf("%d%d", &n, &k);
        scanf("%lf", &t);
        int u = t * 10000 + 0.5;
        multiset<int> S;
        for (int i = 0; i < n; i++) {
            scanf("%lf", &t);
            S.insert(t * 10000 + 0.5);
        }
        while (u--) {
            int t = *S.begin();
            S.erase(S.begin());
            S.insert(t+1);
        }
        double ans = 1;
        for (auto it : S) {
            ans = ans * it / 10000;
        }
        printf("Case #%d: %.9f\n", _, ans);
    }
    return 0;
}
