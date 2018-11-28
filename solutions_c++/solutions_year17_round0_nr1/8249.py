#include <cstdio>
#include <cstring>
using namespace std;
char a[1123];
int main() {
    int T;
    scanf("%d ", &T);
    for (int cs = 1; cs <= T; ++cs) {
        int ans = 0, k;
        scanf("%s %d ", a, &k);
        int L = strlen(a);
        for (int i = 0; i < L; ++i) {
            a[i] = a[i] == '-' ? 0 : 1;
        }
        for (int i = 0; i + k <= L; ++i) {
            if (a[i] == 0) {
                for (int j = i; j < i + k; ++j) {
                    a[j] ^= 1;
                }
                ++ans;
            }
        }
        for (int i = 0; i < L; ++i) {
            if (a[i] == 0) {
                ans = -1;
                break;
            }
        }
        printf("Case #%d: ", cs);
        if (ans == -1) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", ans);
        }
    }
}
