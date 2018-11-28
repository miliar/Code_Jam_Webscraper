#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
ll r[1005], rh[1005];

int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++) {
        int n, m;
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i ++) {
            cin >> r[i] >> rh[i];
            rh[i] *= r[i];
        }
        ll ans = 0;
        double PI = acos(-1.0);

        for(int i = 0; i < n; i ++) {
            vector<ll> V;
            for(int j = 0; j < n; j ++) if(i != j && r[i] >= r[j]) {
                V.push_back(rh[j]);
            }
            sort(V.begin(), V.end());
            int cnt = m - 1;
            ll cur = 0;
            if(V.size() < m - 1) continue;
            for(int j = V.size()-1; j >= 0 && cnt; j --) {
                cur += V[j];
                cnt --;
            }
            cur = 2 * cur + r[i] * r[i] + 2 * rh[i];
            if(cur > ans) ans = cur;
        }

        double anss = ans * PI;

        printf("Case #%d: %.9f\n", kase, anss);
    }
    return 0;
}

