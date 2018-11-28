#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
const int maxn = 2100;
char s[maxn];
int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while (T--) {
        int n, m;
        scanf("%s%d", s+1, &m);
        n = strlen(s+1);
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (s[i] == '-' && i+m-1 <= n) {
                ans++;
                for (int j = 0; j < m; j++) {
                    if (s[i+j] == '-') s[i+j] = '+';
                    else s[i+j] = '-';
                }
            }
        }
        bool ff = true;
        for (int i = 1; i <= n; i++) if (s[i] == '-') ff = false;
        
        printf("Case #%d: ", ++cas);
        
        if (ff) printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
}