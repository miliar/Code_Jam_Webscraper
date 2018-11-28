#include <cstdio>
#include <cassert>
#include <algorithm>
using namespace std;
int mincp(int a, int b) {
    // ceil((a / b) / 1.1)
    // = ..(a / (b * 1.1))
    // = ..((a * 10) / (b * 11))
    a *= 10;
    b *= 11;
    return (a - 1) / b + 1;
}
bool check(long a, long b) {
    // 0.9 * b <= a <= 1.1 * b
    return 9 * b <= 10 * a && 10 * a <= 11 * b;
}

int r[50];
int p[50][50];
int ix[50];
int solve() {
    int n, m;
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++)
        scanf("%d", r + i);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++)
            scanf("%d", p[i] + j);
        sort(p[i], p[i] + m);
    }
    fill_n(ix, n, 0);
    int ans = 0;
    while(none_of(ix, ix + n, [m](int i){ return i >= m; })) {
        int x = 1;
        for(int i = 0; i < n; i++)
            x = max(x, mincp(p[i][ix[i]], r[i]));
        bool ok = true;
        for(int i = 0; i < n; i++)
            if(!check(p[i][ix[i]], (long) r[i] * x)) {
                ok = false;
                ix[i]++;
            }
        if(ok) {
            ans++;
            for(int i = 0; i < n; i++)
                ix[i]++;
        }
#if 0
        for(int i = 0; i < n; i++)
            printf("%d ", ix[i]);
        putchar('\n');
#endif
    }
    return ans;
}
int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        printf("Case #%d: %d\n", i, solve());
    }
}
