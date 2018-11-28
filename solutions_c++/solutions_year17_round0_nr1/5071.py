#include <cstdio>
#include <cstring>
#include "io.h"

const int MAXN = 1000;

char s[MAXN+5];

char get_not(char c) {
    if (c == '+') {
        return '-';
    } else {
        return '+';
    }
}

int main() {
//    init_io("A_eg.in", "A_eg.out");
//    init_io("A-small-attempt0.in", "A-small-attempt0.out");
    init_io("A-large.in", "A-large.out");
    int T;
    int k;
    int ans;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        ans = 0;
        scanf("%s%d", s, &k);
        size_t len = strlen(s);
        for (size_t i = 0; i < len; ++i) {
            if (s[i] == '+') {
                continue;
            } else {
                if (i+k > len) {
                    goto fail;
                }
                for (size_t j = i; j < i+k; ++j) {
                    s[j] = get_not(s[j]);
                }
                ++ans;
            }
        }
        printf("Case #%d: %d\n", t, ans);
        continue;
        fail:
        printf("Case #%d: IMPOSSIBLE\n", t);
    }
    return 0;
}