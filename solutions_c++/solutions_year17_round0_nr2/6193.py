#include <cstdio>
#include <cstring>
using namespace std;
char n[20];
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++ cas) {
        scanf("%s", &n);
        int len = strlen(n), i = 1;
        for (int i = 1; i < len; ++ i) {
            if (n[i - 1] > n[i]) {
                n[-- i] -= 1;
                while (i > 0 && n[i - 1] > n[i]) {
                    n[-- i] -= 1;
                }
                for (int j = i + 1; j < len; ++ j) {
                    n[j] = '9';
                }
                break;
            }
        }
        printf("Case #%d: %s\n", cas, n[0] == '0' ? n + 1 : n);
    }
    return 0;
}
