#include <cstdio>
#include <cstring>

using namespace std;

const int MAXL = 25;

int main() {
    int T;
    scanf("%d", &T);
    char s[MAXL];
    char *pnt;
    size_t slen;
    char min_n;
    for (int t = 1; t <= T; ++t) {
        scanf("%s", s);
        slen = strlen(s);
        pnt = s;
        for (int i = 0; i < slen;) {
            int j = i + 1;
            while (j < slen && s[i] == s[j])
                ++j;
            if (j == slen)
                break;
            if (s[i] > s[j]) {
                --s[i++];
                while (i < slen) {
                    s[i++] = '9';
                }
                break;
            }
            i = j;
        }
        while (*pnt == '0')
            ++pnt;
        printf("Case #%d: %s\n", t, pnt);
    }
}
