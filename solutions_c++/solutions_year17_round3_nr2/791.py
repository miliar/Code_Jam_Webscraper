#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn = 110;
int c[maxn], d[maxn], j[maxn], k[maxn];

int main() {
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ca++) {
        int n, m;
        cin >> n >> m;
        for (int i = 1; i <= n; i++) cin >> c[i] >> d[i];
        for (int i = 1; i <= m; i++) cin >> j[i] >> k[i];
        int ans = 0;
        if (n <= 1 && m <= 1)
            ans = 2;
        else {
            if (n == 2) {
                if (c[1] > c[2]) swap(c[1], c[2]);
                if (d[1] > d[2]) swap(d[1], d[2]);
                if (c[2] - d[1] >= 720 || c[1] + 1440 - d[2] >= 720)
                    ans = 2;
                else
                    ans = 4;
            } else {
                if (j[1] > j[2]) swap(j[1], j[2]);
                if (k[1] > k[2]) swap(k[1], k[2]);
                if (j[2] - k[1] >= 720 || j[1] + 1440 - k[2] >= 720)
                    ans = 2;
                else
                    ans = 4;
            }
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}