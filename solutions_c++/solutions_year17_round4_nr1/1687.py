#include<cstdio>
#include<cinttypes>
#include<algorithm>
using namespace std;
int t[4];
int main() {
    int ttt, tt;
    int n, p, a, ans;
    scanf("%d", &ttt);
    for (int tt = 1; tt <= ttt; tt++) {
        for (int i = 0; i < 4; i++) {
            t[i] = 0;
        }
        scanf("%d", &n);
        scanf("%d", &p);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a);
            t[a%p]++;
        }
        if (p == 2) {
            ans = t[0] + (t[1]+1)/2;
        } else if (p == 3) {
            ans = t[0];
            a = min(t[1], t[2]);
            ans += a;
            t[1] -= a;
            t[2] -= a;
            a = t[1]/3;
            ans += a;
            t[1] -= 3*a;
            a = t[2]/3;
            ans += a;
            t[2] -= 3*a;
            if (t[1] > 0 || t[2] > 0) {
                ans++;
            }
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
