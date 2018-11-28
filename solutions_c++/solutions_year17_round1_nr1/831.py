#include <cstdio>
#include <algorithm>

using namespace std;

const int N = 50;

int T, n, m;
char s[N][N];

int main() {

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf("%s", s[i]);
        }
        int p = 0;
        for (int i = 0; i < m; i++) {
            char c = '?';
            for (int j = 0; j < n; j++) {
                if (s[j][i] != '?') {
                    c = s[j][i];
                    break;
                }
            }
            for (int j = 0; j < n; j++) {
                if (s[j][i] == '?') {
                    s[j][i] = c;
                } else {
                    c = s[j][i];
                }
            }
        }
        for (int i = 1; i < m; i++) {
            if (s[0][i] != '?') {
                continue;
            }
            for (int j = 0; j < n; j++) {
                s[j][i] = s[j][i - 1];
            }
        }
        for (int i = m - 2; i >= 0; i--) {
            if (s[0][i] != '?') {
                continue;
            }
            for (int j = 0; j < n; j++) {
                s[j][i] = s[j][i + 1];
            }
        }
        printf("Case #%d:\n", t);
        for (int i = 0; i < n; i++) {
            printf("%s\n", s[i]);
        }
    }

    return 0;

}

