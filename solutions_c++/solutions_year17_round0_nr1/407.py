#include <cstdio>
#include <cstring>

using namespace std;

char s[1001];

int main() {
    int t, i;
    
    scanf("%d", &t);
    
    for (i = 0; i < t; i++) {
        int k, n, ans = 0, j, l;
        
        scanf("%s %d", s, &k);
        
        n = strlen(s);
        
        for (j = 0; j + k <= n; j++) {
            if (s[j] == '-') {
                ans++;
                
                for (l = 0; l < k; l++) {
                    if (s[j + l] == '-') {
                        s[j + l] = '+';
                    } else {
                        s[j + l] = '-';
                    }
                }
            }
        }
        
        for (j = 0; j < n; j++) {
            if (s[j] == '-') {
                ans = -1;
                
                break;
            }
        }
        
        printf("Case #%d: ", i + 1);
        if (ans >= 0) {
            printf("%d\n", ans);
        } else {
            puts("IMPOSSIBLE");
        }
    }
    
    return 0;
}
