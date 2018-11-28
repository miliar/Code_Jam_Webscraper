#include <iostream>
using namespace std;
int main() {
    int T;
    char str[2000];
    int l[2000];
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%s", str);
        int k, len = strlen(str), s = 0, ans = 0;
        scanf("%d", &k);
        memset(l, 0, sizeof(l));
        for (int i = 0; i + k - 1 < len; ++i) {
            s = (s + l[i]) % 2;
            if (s == (str[i] == '+')) {
                s = 1 - s;
                l[i + k] += 1;
                ans++;
            }
        }
        bool flag = true;
        for (int i = max(0, len - k + 1); i < len; ++i) {
            s = (s + l[i]) % 2;
            if (s == (str[i] == '+')) {
                flag = false;
                break;
            }
        }
        printf("Case #%d: ", ca);
        if (!flag) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", ans);
        }
    }
    return 0;
}
