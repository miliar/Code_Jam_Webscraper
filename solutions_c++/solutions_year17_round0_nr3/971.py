#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>


using namespace std;

typedef __int64 lld;
typedef pair<lld, lld> PII;
const lld INF = 1LL<<61;

inline lld mx(lld a, lld b) {return a > b ? a : b;}
inline lld mi(lld a, lld b) {return a < b ? a : b;}

map<PII, PII> result;

PII dfs(lld n, lld k) {
    lld l, r;
    l = (n - 1) / 2;
    r = n - 1 - l;
    if (k == 0) {
        return make_pair(INF, INF);
    }
    if (k == 1) {
        return make_pair(mx(l, r), mi(l, r));
    }
    PII key = make_pair(n, k);
    if (result.find(key) != result.end()) {
        return result[key];
    }
    k --;
    lld kl = k / 2;
    lld kr = k - kl;
    PII retl = dfs(l, kl), retr = dfs(r, kr);
    if (retl < retr) {
        return result[key] = retl;
    } else  {
        return result[key] = retr;
    }
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C2.out", "w", stdout);
    int T;
    lld n, k;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%I64d %I64d", &n, &k);
        PII ans = dfs(n, k);
        lld y = ans.first, z = ans.second;
        printf("Case #%d: %I64d %I64d\n", cas, y, z);
        result.clear();
    }
    return 0;
}
