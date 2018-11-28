#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

#define MAXN 100010
#define INF 0x3f3f3f3f
typedef long long LL;

int T;
LL n, k;

void F(LL a, LL b, LL c, LL d, LL &e, LL &f, LL &g, LL &h)
{
    e = a / 2; f = (b - 1) / 2;
    g = c; h = d;
    if(a & 1) g += c;
    else h += c;
    if(b & 1) h += d;
    else g += d;
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int j;
    LL l, r, cnt[2], len[2];
    for(scanf("%d", &T), j = 1; j <= T; ++j){
        scanf("%I64d %I64d", &n, &k);
        len[0] = n; cnt[0] = 1;
        len[1] = n; cnt[1] = 0;
        while(k > 0){
            if(cnt[0] >= k){
                l = len[0] / 2;
                r = len[0] - l - 1;
                break;
            }
            if(cnt[0] + cnt[1] >= k){
                l = len[1] / 2;
                r = len[1] - l - 1;
                break;
            }
            k -= cnt[0] + cnt[1];
            F(len[0], len[1], cnt[0], cnt[1], len[0], len[1], cnt[0], cnt[1]);
        }

        printf("Case #%d: %I64d %I64d\n", j, max(l, r), min(l, r));
    }
    return 0;
}
