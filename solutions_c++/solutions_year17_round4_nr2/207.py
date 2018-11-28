#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAXN 1010
typedef long long LL;

int n, m, c, p, b, T;
int cnt[MAXN], seat[MAXN];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int i, j, ans, res, l, r, mid;
    for(scanf("%d", &T), j = 1; j <= T; ++j){
        memset(seat, 0, sizeof(seat));
        memset(cnt, 0, sizeof(cnt));
        scanf("%d %d %d", &n, &c, &m);
        for(i = 1; i <= m; ++i){
            scanf("%d %d", &p, &b);
            ++cnt[b]; ++seat[p];
        }
        l = seat[1]; r = m;
        for(i = 1; i <= c; ++i)
            l = max(l, cnt[i]);
        for(; l < r;){
            mid = (l + r) >> 1;
            for(i = n, ans = 0, res = 0; i; --i){
                if(seat[i] > mid){
                    ans += seat[i] - mid;
                    res += seat[i] - mid;
                }
                else{
                    if(mid - seat[i] < res)
                        res -= mid - seat[i];
                    else res = 0;
                }
            }
            if(!res) r = mid;
            else l = mid + 1;
        }
        for(i = n, ans = 0, res = 0; i; --i){
            if(seat[i] > r){
                ans += seat[i] - r;
                res += seat[i] - r;
            }
            else{
                if(r - seat[i] < res)
                    res -= r - seat[i];
                else res = 0;
            }
        }
        printf("Case #%d: %d %d\n", j, r, ans);
    }
}
