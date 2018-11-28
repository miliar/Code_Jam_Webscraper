#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAXN = 1024;

bool valid(char *s) {

    for (int i = 0; s[i]; ++i) {

        if (s[i] == '-')
            return false;
    }

    return true;
}

int main() {

    int t, k;
    char s[MAXN];

    scanf("%d", &t);

    for (int no = 1; no <= t; ++no) {

        scanf("%s %d", s, &k);

        int ans = 0;
        int n = strlen(s);

        for (int i = 0; i <= n - k; ++i) {

            if (s[i] == '-') {

                ans++;

                for (int j = i; j < i + k; ++j)
                    s[j] = (s[j] == '-') ? '+' : '-';
            }
        }

        printf("Case #%d: ", no);
        if (valid(s))
            printf("%d\n", ans);
        else printf("IMPOSSIBLE\n");
    }
}
