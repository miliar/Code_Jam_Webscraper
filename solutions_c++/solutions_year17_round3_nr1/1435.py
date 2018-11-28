#include <bits/stdc++.h>
using namespace std;

struct cake{
    long long r, h;
    bool operator <(cake other) const {
        return r < other.r;
    }
};

long long memo[2][1005][1005];
int n, k;
cake arr[1005];

long long f(int ud, int n, int k) {
    if (k == 0)
        return 0;
    if (n == 0)
        return -999999999999;

    long long &ret = memo[ud][n][k];
    if (ret != -1)
        return ret;

    ret = f(ud, n-1, k);

    if (ud == 1)
        ret = max(ret, f(ud, n-1, k-1) + 2 * arr[n].r * arr[n].h);
    if (ud == 0)
        ret = max(ret, f(1, n-1, k-1) + 2 * arr[n].r * arr[n].h + arr[n].r * arr[n].r);

    return ret;

}

void bt(int ud, int n, int k) {
    if (k == 0 || n == 0)
        return;

    if (f(ud, n, k) == f(ud, n-1, k-1))
        bt(ud, n-1, k-1);

    if (ud == 1)
        if (f(ud, n-1, k-1) + 2 * arr[n].r * arr[n].h == f(ud, n, k)){
            printf("->%lld %lld\n", arr[n].r, arr[n].h);
            bt(ud, n-1, k-1);
        }

    if (ud == 0)
        if (f(1, n-1, k-1) + 2 * arr[n].r * arr[n].h + arr[n].r * arr[n].r == f(ud, n, k)) {
            printf("->%lld %lld\n", arr[n].r, arr[n].h);
            bt(1, n-1, k-1);
        }
}

int main() {
    int TC;
    scanf("%d", &TC);
    for (int zz = 1; zz <= TC; zz++) {
        memset(memo, -1, sizeof(memo));

        scanf("%d %d", &n, &k);
        for (int i = 1; i <= n; i++) {
            scanf("%lld %lld", &arr[i].r, &arr[i].h);
        }

        sort(arr+1, arr+1+n);

        // for (int i = 1; i <= n; i++) {
        //     printf("%lld %lld\n", arr[i].r, arr[i].h);
        // }

        long long ans = f(0, n, k);
        // bt(0, n, k);
        double jaw = ans * acos(-1);
        printf("Case #%d: %.9f\n", zz, jaw);
        // printf("%lld\n", ans);
    }
}