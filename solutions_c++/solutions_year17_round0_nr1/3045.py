#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        char chr[1024];
        int k;
        scanf("%s%d", chr, &k);
        int l = strlen(chr);
        bool bol[1024];
        for (int i = 0; i < l; i++) {
            bol[i] = (chr[i] == '+');
        }
        int res = 0;
        for (int i = 0; i <= l - k; i++) {
            if (!bol[i]) {
                for (int j = 0; j < k; j++) {
                    bol[i + j] ^= 1;
                }
                res++;
            }
        }
        bool ok = 1;
        for (int i = l - k + 1; i < l; i++) {
            ok &= bol[i];
        }
        printf("Case #%d: ", tc);
        if (ok) {
            printf("%d", res);
        } else {
            printf("IMPOSSIBLE");
        }
        printf("\n");
    }
}
