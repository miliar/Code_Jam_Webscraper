#include <cstdio>
#include <cstring>
using namespace std;
const int N = 1005;
char s[N];
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, k;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++ cas) {
        scanf("%s%d", &s, &k);
        int n = strlen(s), cnt = 0;
        for (int i = 0; i < n && ~cnt; ++ i) {
            if (s[i] == '-') {
                ++ cnt;
                for (int j = 0; j < k; ++ j) {
                    if (i + j >= n) {
                        cnt = -1;
                        break;
                    }
                    s[i + j] = s[i + j] == '-' ? '+' : '-';
                }
            }
        }
        printf("Case #%d: ", cas);
        if (~cnt) {
            printf("%d\n", cnt);
        } else {
            puts("IMPOSSIBLE");
        }
    }
    return 0;
}
