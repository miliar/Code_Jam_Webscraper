#include <bits/stdc++.h>
using namespace std;
const int N = 100005;

int t, tc, n, p, g[N];
int f[4];

int pick_two(int a, int b, int p) {
    if (a > b) swap(a, b);
    int ans = a + (b - a + p - 1) / p;
    return ans;
}

int main() {
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++tc);
        scanf("%d", &n);
        scanf("%d", &p);
        memset(f, 0, sizeof f);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &g[i]);
            f[g[i]%p] += 1;
        }
        int ans = f[0];
        if (p == 2) {
            ans += (f[1] + 1) / 2;
        } else if (p == 3) {
            ans += pick_two(f[1], f[2], 3);
        } else if (p == 4) {
            ans += (f[2] + 1) / 2; // 2,2,2 ...
            if (f[2] % 2 == 0) {
                ans += pick_two(f[1], f[3], 4);
            } else {
                // special Case
                if (f[1] >= 2 || f[3] >= 2) {
                    int mn = INT_MAX;
                    if (f[1] >= 2)
                        mn = min(mn, ans + pick_two(f[1]-2, f[3], 4)); // add 1,1 first
                    if (f[3] >= 2)
                        mn = min(mn, ans + pick_two(f[1], f[3]-2, 4)); // add 3,3 first
                    ans = mn;
                } else {
                    // nothing happens, cannot unfold
                }
            }
        }
        printf("%d\n", ans);


    }
}
