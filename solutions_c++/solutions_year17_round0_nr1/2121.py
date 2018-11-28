#include <cstdio>
#include <cstring>

#define LMAX_LARGE 1000

int main()
{
    int t;
    static char s[LMAX_LARGE+2];

    scanf("%d", &t);
    for (int tc = 1; tc <= t; ++tc) {
        int len, k;
        int flips = 0;
        int correct = 0;

        scanf("%s %d", s, &k);
        len = strlen(s);
        for (int i = 0; i <= len-k; ++i) {
            if (s[i] == '-') {
                for (int j = i; j < i+k; ++j) {
                    s[j] ^= (char)6;
                }
                ++flips;
            }
        }

        for (int i = 0; i < len; ++i) {
            if (s[i] == '+')
                ++correct;
        }

        printf("Case #%d: ", tc);
        if (correct == len) {
            printf("%d\n", flips);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }

    return 0;
}
