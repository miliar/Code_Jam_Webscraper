#include <cstdio>
#include <cstring>

int main() {
    int n, s, count;
    scanf("%d",&n);
    char str[1001];
    int impossible = 0;
    for (int i = 0; i < n; ++i) {
        scanf("%s",str);
        scanf("%d",&s);
        impossible = 0;
        count = 0;
        for (int j = 0; str[j+s-1] != '\0'; j++) {
            if (str[j] == '-') {
                for (int k = 0; k < s; ++k) {
                    str[j+k] = (str[j+k] == '-') ? '+' : '-';
                }
                ++count;
            }
        }
        int len = strlen(str);
        for (int j = len-1; j >= len-s; --j) {
            if (str[j] == '-') {
                impossible = 1;
                break;
            }
        }
        if (impossible == 1) printf("Case #%d: IMPOSSIBLE\n", i+1);
        else printf("Case #%d: %d\n", i+1, count);
    }
}
