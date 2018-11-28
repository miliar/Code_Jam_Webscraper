#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

#define MAXN 100010
#define INF 0x3f3f3f3f
typedef long long LL;

int T, n, k, a[MAXN];
char s[MAXN];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int i, j, cnt, ans;
    for(scanf("%d", &T), j = 1; j <= T; ++j){
        scanf("%s %d", s, &k);
        n = strlen(s); cnt = ans = 0;
        for(i = 0; i < n; ++i){
            if(i - k >= 0) cnt -= a[i - k];
            if(i <= n - k){
                if(s[i] == '+'){
                    if(cnt & 1) a[i] = 1, ++ans, ++cnt;
                    else a[i] = 0;
                }
                else{
                    if(cnt & 1) a[i] = 0;
                    else a[i] = 1, ++ans, ++cnt;
                }
            }
            else{
                if(s[i] == '+'){
                    if(cnt & 1) ans = -1;
                }
                else{
                    if(cnt & 1);
                    else ans = -1;
                }
            }
        }

        printf("Case #%d: ", j);
        if(ans == -1) printf("IMPOSSIBLE");
        else printf("%d", ans);
        printf("\n");
    }
    return 0;
}
