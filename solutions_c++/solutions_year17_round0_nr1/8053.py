#include <string>
#include <cstdio>
#include <cstring>

int main() {
    int n, k;
    char s[1005];
    scanf("%d", &n);
    for(int cas = 1; cas <= n; cas++) {
        scanf("%s %d", s, &k);
        int ans = 0, len = strlen(s);
        for(int i = 0; i < len; i++) {
            if(s[i] == '+') {
                continue;
            }
            if(i+k-1 >= len) {
                ans = -1;
                break;
            }
            ans++;
            for(int j = 0; j < k; j++) {
               if(s[i+j] == '+') {
                   s[i+j] = '-';
               } else {
                   s[i+j] = '+';
               }
            }
        }
        if(ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
        } else {
            printf("Case #%d: %d\n", cas, ans);
        }
    }
        
}
