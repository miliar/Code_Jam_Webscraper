#include <cstdio>
#include <cstring>
#include <climits>
#include <algorithm>
using namespace std;
const int MAXN = 101;

int f[MAXN][MAXN][MAXN * 4][MAXN];
int hd, ad, hk, ak, b, d;

int DP(int i, int j, int k, int l) {
    int &ret = f[i][j][k][l];
    if (ret != -1) return ret;
    ret = INT_MAX;
    //printf("%d %d %d %d: %d\n", i, j, k, l, f[i][j][k][l]);
    //attack
    if (k >= j) return ret = 1;
    if (i > l) {
        int next = DP(i - l, j - k, k, l);
        if (next < ret) ret = next;
    }
    //buff
    if (b > 0 && i > l && k + b < MAXN * 4) {
        int next = DP(i - l, j, k + b, l);
        if (next < ret) ret = next;
    }
    //cure
    if (i < hd - l) {
        int next = DP(hd - l, j, k, l);
        if (next < ret) ret = next;
    }
    //debuff
    int _ak = l - d;
    if (_ak < 0) _ak = 0;
    if (d > 0 && l > 0 && i > _ak) {
        int next = DP(i - _ak, j, k, _ak);
        if (next < ret) ret = next;
    }
    if (ret != INT_MAX) ret++;
    return ret;
}

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
        memset(f, 0xff, sizeof(f));
        DP(hd, hk, ad, ak);
        if (f[hd][hk][ad][ak] == INT_MAX) printf("Case #%d: IMPOSSIBLE\n", cas);
        else printf("Case #%d: %d\n", cas, f[hd][hk][ad][ak]);
    }
    return 0;
}
