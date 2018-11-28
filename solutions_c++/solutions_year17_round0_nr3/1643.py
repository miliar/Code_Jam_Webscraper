#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

typedef long long LL;

map<LL, LL> cnt;
map<LL, LL>::iterator it;
LL ans, n, k, now, lf, rt;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, kase = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%I64d%I64d", &n, &k);
        cnt.clear();
        cnt[n] = 1;
        while (k) {
            it = cnt.end();
            --it;
            if (k <= it -> second) {
                ans = it -> first - 1;
//                cout << ans << endl;
                break;
            }
            k -= it -> second;
            now = it -> first;
            --now;
            lf = now / 2 + now % 2;
            rt = now / 2;
            cnt[lf] += it -> second;
            cnt[rt] += it -> second;
            cnt.erase(it);
        }
        printf("Case #%d: %I64d %I64d\n", ++kase, (ans + 1) / 2, ans / 2);
    }
}
