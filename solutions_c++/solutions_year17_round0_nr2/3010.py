#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int tc = 1; tc <= t; tc++) {
        char chr[32];
        scanf("%s", chr);
        int l = strlen(chr);
        for (int i = l - 1; i > 0; i--) {
            if (chr[i] < chr[i - 1]) {
                for (int j = i; j < l; j++) {
                    chr[j] = '9';
                }
                chr[i - 1] -= 1;
            }
        }
        bool ok = 0;
        printf("Case #%d: ", tc);
        for (int i = 0; i < l; i++) {
            if (chr[i] == '0' && !ok) {
                continue;
            }
            ok |= (chr[i] != '0');
            printf("%c", chr[i]);
        }
        printf("\n");
    }
}
