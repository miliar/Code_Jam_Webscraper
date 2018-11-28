#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 1e3 + 5;

int TC, tc, N;
char s[MAXN];
int f[MAXN];

int main() {
    freopen("i.in", "r", stdin);
    freopen("o.out", "w", stdout);
    scanf("%d", &TC);
    while(TC--) {
        scanf("%s%d", s, &N);
        int M = strlen(s);
        for(int i = 0; i < M; i++)
            f[i] = false;
        bool inv = false;
        int ans = 0, i;
        for(i = 0; i + N <= M; i++) {
            if(f[i]) inv = !inv;
            if((s[i] == '-') ^ inv) {
                inv = !inv;
                f[i + N] = true;
                ans++;
            }
        }
        bool ex = true;
        for( ; i < M; i++) {
            if(f[i]) inv = !inv;
            if((s[i] == '-') ^ inv)
                ex = false;
        }
        if(ex)
            printf("Case #%d: %d\n", ++tc, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", ++tc);
    }
}
