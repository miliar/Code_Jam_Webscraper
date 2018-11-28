#include <cstdio>

#define N 64

int T, n;
char s[N];
bool f;

int main() {
    scanf("%d", &T);
    for (int r = 1; r <= T; ++r) {
        printf("Case #%d: ", r);
        scanf("%s", s);
        n = -1;
        while (s[++n]);
        for (int i = 0; i < n; ++i) {
            f = 1;
            for (int j = i + 1; j < n; ++j) {
                if (s[j] < s[i]) {
                    f = 0;
                    break;
                }
                if (s[i] < s[j])
                    break;
            }
            if (!f) {
                --s[i];
                for (int j = i + 1; j < n; ++j)
                    s[j] = '9';
                break;
            }
        }
        n = 0;
        while (s[n] == '0')
            ++n;
        puts(s + n);
    }
    return 0;
}
