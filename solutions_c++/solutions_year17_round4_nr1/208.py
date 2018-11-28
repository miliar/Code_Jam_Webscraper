#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;

int n, p, g, T;
int cnt[10];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int i, j;
    for(scanf("%d", &T), j = 1; j <= T; ++j){
        cnt[0] = cnt[1] = cnt[2] = cnt[3] = 0;
        scanf("%d %d", &n, &p);
        for(i = 1; i <= n; ++i){
            scanf("%d", &g);
            ++cnt[g % p];
        }
        if(p == 2){
            printf("Case #%d: %d\n", j, cnt[0] + (cnt[1] + 1) / 2);
        }
        else if(p == 3){
            printf("Case #%d: %d\n", j, cnt[0] + min(cnt[1], cnt[2]) + (abs(cnt[1] - cnt[2]) + 2) / 3);
        }
        else{
            printf("Case #%d: %d\n", j, cnt[0] + min(cnt[1], cnt[3]) + (abs(cnt[1] - cnt[3]) + cnt[2] * 2 + 3) / 4);
        }
    }
}
