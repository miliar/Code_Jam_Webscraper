#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int MAXL = 1010;

int main() {
    int T;
    scanf("%d", &T);
    int ans = -1;
    char s[MAXL];
    int k;
    size_t slen;
    for (int t = 1; t <= T; ++t) {
        scanf("%s %d", s, &k);
        slen = strlen(s);
        ans = 0;
        for (int i = 0; i < slen; ++i) {
            if (s[i] == '-') {
                if (i + k > slen) {
                    ans = -1;
                    break;
                } else {
                    ++ans;
                    int j = 0;
                    while (j < k) {
                        s[i+j] = '-' - s[i+j] + '+';
                        ++j;
                    }
                }
            }
        }
        printf("Case #%d: ", t);
        if (ans == -1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
}
