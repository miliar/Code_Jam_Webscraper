#include <cstdio>
#include <cstring>
#include <cstdlib>

char s[10001];

int main()
{
    int tests, test = 1;
    for (scanf("%d", &tests); test <= tests; ++ test) {
        int k;
        scanf("%s%d", s, &k);
        int n = strlen(s);
        bool possible = true;
        int cnt = 0;
        for (int i = 0; i < n; ++ i) {
            if (s[i] == '-') {
                if (i + k > n) {
                    possible = false;
                    break;
                }
                ++ cnt;
                for (int j = 0; j < k; ++ j) {
                    s[i + j] = '+' + '-' - s[i + j];
                }
            }
        }
        if (possible) {
            printf("Case #%d: %d\n", test, cnt);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", test);
        }
    }
    return 0;
}
