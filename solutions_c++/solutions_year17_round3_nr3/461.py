#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

double P[55];

int main() {
    freopen("C.in", "r", stdin);
    freopen("C2.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++) {
        int n, k;
        cin >> n >> k;
        double u;
        cin >> u;
        for(int i = 0; i < n; i ++) cin >> P[i];
        sort(P, P + n);
        P[n] = 1;

        double cur = P[0];
        int cnt = 1;
        for(int i = 1; i <= n; i ++) {
            if(u <= 0) break;
            double ret = P[i] - cur;
            double need = ret * cnt;
            if(need <= u) {
                u -= need;
                for(int j = 0; j < i; j ++) P[j] = P[i];
                cur = P[i];
                cnt ++;
            } else {
                need = u / cnt;
                for(int j = 0; j < i; j ++) P[j] += need;
                break;
            }
        }
        double ans = 1;
        for(int i = 0; i < n; i ++) ans *= P[i];

        printf("Case #%d: %.9f\n", kase, ans);
    }
    return 0;
}

