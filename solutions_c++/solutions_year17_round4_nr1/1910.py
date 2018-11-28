#include <cstdio>
#include <algorithm>
#include <cstring>

int n, p;
int a[4];

int main()
{
    int T_T, t_t;
    scanf("%d", &T_T);
    for (t_t = 1; t_t <= T_T; ++t_t) {
        scanf("%d%d", &n, &p);
        for (int i = 1; i <= 3; ++i) {
            a[i] = 0;
        }
        int res = 0;
        for (int i = 1; i <= n; ++i) {
            int x;
            scanf("%d", &x);
            if (x % p != 0) {
                a[x % p]++;           
            } else {
                res ++;
            }
        }
        if (p == 2) {
            res += a[1] + 1 >> 1;
        } else if (p == 3) {
            res += std::min(a[1], a[2]);
            int tmp = std::max(a[1] - a[2], a[2] - a[1]);
            res += (tmp + 2) / 3;
        } else if (p == 4) {
            res += a[2] >> 1;
            res += std::min(a[1], a[3]);
            a[1] -= std::min(a[1], a[3]);
            a[3] -= std::min(a[1], a[3]);
            a[2] &= 1;
            res += (a[1] + a[2] + a[3] + 2 >> 2);
        }
        printf("Case #%d: %d\n", t_t, res);
    }
}
