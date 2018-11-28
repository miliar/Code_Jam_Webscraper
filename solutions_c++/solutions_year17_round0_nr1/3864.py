#include <stdio.h>
#include <vector>
using namespace std;
int main() {
    int t, cas = 0;
    int ans;
    int k;
    char s[1005];
    int pos[1005];
    scanf("%d", &t);
    while (t--) {
        cas++;
        ans = 0;
        scanf("%s", s);
        scanf("%d", &k);
        int l = strlen(s);
        memset(pos, 0, sizeof(pos));
        if (s[0] == '-') {
            pos[0] = 1;
        }
        if (s[l - 1] == '-') {
            pos[l] = 1;
        }
        for (int i = 0; i < l - 1; ++i) {
            if (s[i] != s[i+1]) {
                pos[i + 1] = 1;
            }
        }
        for (int i = 0; i <= l - k; ++i) {
            if (pos[i] == 1) {
                pos[i] = 0;
                pos[i + k] ^= 1;
                ans++;
            }
        }
        bool imp = false;
        for (int i = 0; i <= l; ++i) {
            if (pos[i] == 1) {
                imp = true;
                break;
            }
        }
        if (imp) {
            printf("Case #%d: IMPOSSIBLE\n", cas);
        } else {
            printf("Case #%d: %d\n", cas, ans);
        }
    }
    return 0;
}
