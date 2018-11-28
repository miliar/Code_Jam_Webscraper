#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int ans;
int n, p;
int f[10];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        ans = 0;
        memset(f, 0, sizeof(f));
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; ++i) {
            int x;
            scanf("%d", &x);
            ++f[x % p];
        }
        ans = f[0];
        if (p == 2) {
            ans += (f[1] + 1) / 2;
        }
        if (p == 3) {
            int num = min(f[1], f[2]);
            ans += num;
            f[1] -= num;
            f[2] -= num;
            ans += (f[1] + f[2] + 2) / 3;
        }
        if (p == 4) {
            int num = min(f[1], f[3]);
            ans += num;
            f[1] -= num;
            f[3] -= num;
            ans += f[2] / 2;
            f[2] %= 2;
            if (f[2] > 0) {
                num = f[1] + f[3] - 2;
                ++ans;
                if (num > 0) {
                    ans += (num + 3) / 4;
                }
            } else {
                ans += (f[1] + f[3] + 3) / 4;
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}