#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const double PI = acos(-1);

const int N = 1e3 + 10;
int r[N], h[N];

int main() {
    int T;
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++) {
        int n, k;
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; i++) {
            scanf("%d%d", r + i, h + i);
        }
        double ans = 0;
        for (int i = 0; i < n; i++) {
            double tans = 2 * PI * r[i] * h[i] + PI * r[i] * r[i]; 
            vector<double> v;
            for (int j = 0; j < n; j++) if (i != j && r[j] <= r[i]) {
                v.push_back(2 * PI * r[j] * h[j]);
            }
            if ((int)v.size() >= k - 1) {
                sort(v.begin(), v.end());
                reverse(v.begin(), v.end());
                for (int j = 0; j < k - 1; j++) tans += v[j];
                ans = max(ans, tans);
            }
        }
        printf("Case #%d: %.9f\n", _, ans);
    }
    return 0;
}
