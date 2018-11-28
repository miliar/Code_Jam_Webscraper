#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int maxn = 30;
char s[maxn];

int main() {
    int tt;
    scanf("%d\n", &tt);
    for (int t = 1; t <= tt; t++) {
        scanf("%s", s);
        int l = strlen(s);
        bool f = false;
        for (int i = 0; i < l - 1 && !f; i++)
            if (s[i] > s[i + 1]) f = true;
        if (f) {
            for (int i = l - 1; i > 0; i--) {
                if (s[i] < s[i - 1]) {
                    s[i] = '9';
                    s[i - 1] -= 1;
                }
            }
            for (int i = 0; i < l - 1; i++)
                if (s[i] > s[i + 1])
                    s[i + 1] = s[i];
        }
        char * ss = s;
        while (*ss && *ss == '0')
            ss++;
        printf("Case #%d: %s\n", t, ss);
    }
    return 0;
}
