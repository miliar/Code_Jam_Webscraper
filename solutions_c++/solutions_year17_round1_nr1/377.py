#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn = 25 + 5;
char mp[maxn][maxn];
int r, c;
int main() {
    int T; scanf("%d", &T);
    for (int Cas = 1; Cas <= T; Cas++) {
        scanf("%d%d", &r, &c);
        for (int i = 0; i < r; i++) {
            scanf("%s", mp[i]);
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                char c = mp[i][j];
                if (c == '?') continue;
                for (int k = j + 1; k < c; k++) {
                    if (mp[i][k] == '?') {
                        mp[i][k] = c;
                    } else break;
                }
            }
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                char c = mp[i][j];
                if (c == '?') continue;
                for (int k = j - 1; k >=0; k--) {
                    if (mp[i][k] == '?') {
                        mp[i][k] = c;
                    } else break;
                }
            }
        }

        for (int i = 0; i < r; i++) {
            if (mp[i][0] == '?') continue;
            for (int k = i + 1; k < r; k++) {
                if (mp[k][0] == '?') {
                    strcpy(mp[k], mp[i]);
                } else break;
            }
            for (int k = i - 1; k >= 0; k--) {
                if (mp[k][0] == '?') {
                    strcpy(mp[k], mp[i]);
                } else break;
            }
        }
        printf("Case #%d:\n", Cas);
        for (int i = 0; i < r; i++) {
            puts(mp[i]);
        }
    }
}
