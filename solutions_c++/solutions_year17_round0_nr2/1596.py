#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;

LL n;
int len, bit[30], ans[30];
bool flag;

void dfs(int len, int last, bool lim, bool zero) {
    if (len == -1) flag = true;
    if (flag) return ;
    int mx = lim ? bit[len] : 9;
    for (int i = mx; i >= last; --i) {
        ans[len] = i;
        dfs(len - 1, i, i == mx && lim, i == 0 && zero);
        if (flag) return;
    }
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, kase = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%I64d", &n);
        len = 0;
        while (n) {
            bit[len++] = n % 10;
            n /= 10;
        }
        flag = false;
        for (int i = bit[len - 1]; i >= 0; --i) {
            ans[len - 1] = i;
            dfs(len - 2, i, i == bit[len - 1], i == 0);
            if (flag) break;
        }
        for (int i = len - 1; i >= 0; --i) {
            n *= 10;
            n += ans[i];
        }
        printf("Case #%d: %I64d\n", ++kase, n);
    }
}
