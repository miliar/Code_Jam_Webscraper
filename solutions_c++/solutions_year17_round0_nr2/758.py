#include <cstdio>
#include <queue>
#include <cstring>

using namespace std;

#define MAXN 100010
#define INF 0x3f3f3f3f
typedef long long LL;

int T, n;
char s[MAXN];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
//    freopen("removing.in", "r", stdin);
//    freopen("removing.out", "w", stdout);
    int i, j;
    for(scanf("%d", &T), j = 1; j <= T; ++j){
        scanf("%s", s);
        n = strlen(s);
        for(i = 0; i < n - 1; ++i)
            if(s[i] > s[i + 1]) break;
        if(i < n - 1){
            for(; i > 0; --i)
                if(s[i] != s[i - 1]) break;
            --s[i];
            for(++i; i < n; ++i)
                s[i] = '9';
        }
        for(i = 0; i < n; ++i)
            if(s[i] != '0') break;
        printf("Case #%d: ", j);
        for(i = min(n - 1, i); i < n; ++i)
            printf("%c", s[i]);
        printf("\n");
    }
    return 0;
}
