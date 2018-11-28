#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

using ll = long long;

int T;
int f1[101][2];
int f2[101][101][3];
int f3[101][101][101][4];

int dp2(int s1, int res) {
    if (s1 == 0)
        return 0;
    if (f1[s1][res] > -1)
        return f1[s1][res];
    int rst = 0;
    rst = dp2(s1 - 1, (res + 1) % 2);
    if (res == 0)
        rst += 1;
    return f1[s1][res] = rst;
}

int dp3(int s1, int s2, int res) {
    if (s1 + s2 == 0)
        return 0;
    if (f2[s1][s2][res] > -1)
        return f2[s1][s2][res];
    int rst = 0;
    if (s1 > 0)
        rst = max(rst, dp3(s1 - 1, s2, (res + 1) % 3));
    if (s2 > 0)
        rst = max(rst, dp3(s1, s2 - 1, (res + 2) % 3));
    if (res == 0)
        rst += 1;
    return f2[s1][s2][res] = rst;
}

int dp4(int s1, int s2, int s3, int res) {
    if (s1 + s2 + s3 == 0)
        return 0;
    if (f3[s1][s2][s3][res] > -1)
        return f3[s1][s2][s3][res];
    int rst = 0;
    if (s1 > 0)
        rst = max(rst, dp4(s1 - 1, s2, s3, (res + 1) % 4));
    if (s2 > 0)
        rst = max(rst, dp4(s1, s2 - 1, s3, (res + 2) % 4));
    if (s3 > 0)
        rst = max(rst, dp4(s1, s2, s3 - 1, (res + 3) % 4));
    if (res == 0)
        rst += 1;
    return f3[s1][s2][s3][res] = rst;
}

int main() {
    scanf("%d", &T);
    memset(f1, -1, sizeof(f1));
    memset(f2, -1, sizeof(f2));
    memset(f3, -1, sizeof(f3));
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        int n, p;
        scanf("%d%d", &n, &p);
        int ans = 0, t;
        int s[4];
        memset(s, 0, sizeof(int) * 4);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &t);
            s[t % p] ++;
        }
        if (p == 2)
            ans = s[0] + dp2(s[1], 0);
        if (p == 3)
            ans = s[0] + dp3(s[1], s[2], 0);
        if (p == 4)
            ans = s[0] + dp4(s[1], s[2], s[3], 0);
        printf("%d\n", ans);
    }
    return 0;
}