#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 1005;
char str[N];
int a[N], K;


int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%s%d", str, &K);
        int n = strlen(str);
        for (int i = 0; i < n; ++i) {
            a[i] = (str[i] == '+');
        }
        int ans = 0, flag = 1;
        for (int i = 0; i < n; ++i) {
            if (a[i] == 1) {
                continue;
            } else {
                if (i + K > n) {
                    flag = 0;
                    break;
                } else {
                    for (int j = 0; j < K; ++j) {
                        a[j + i] ^= 1;
                    }
                    ans += 1;
                }
            }
        }
        printf("Case #%d: ", cas);
        if (flag == 0) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", ans);
        }
    }
    return 0;
}
