#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
#define TASK "A-large"
    freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cs = 1; cs <= t; ++cs) {
        printf("Case #%d:\n", cs);
        int r, c;
        char m[30][30];
        map<char, pair<int, int>> l;
        map<pair<int, int>, pair<int, int>> rect;
        scanf("%d %d\n", &r, &c);
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                scanf("%c", &m[i][j]);
                if (m[i][j] != '?') {
                    auto it = l.find(m[i][j]);
                    if (it != l.end()) {
                        auto it2 = rect.find(it->second);
                        if (it2 == rect.end()) {
                            rect[it->second] = make_pair(i, j);
                        } else {
                            rect[it->second] = make_pair(max(i, it2->second.first),
                                                         max(j, it2->second.second));
                        }
                    } else l[m[i][j]] = make_pair(i, j);
                }
            }
            char n;
            scanf("%c", &n);
        }
        for (auto it = rect.begin(); it != rect.end(); ++it) {
            for (int i = it->first.first; i < it->second.first; ++i)
                for (int j = it->first.second; j < it->second.second; ++j)
                    m[i][j] = m[it->first.first][it->first.second];
        }
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                if (m[i][j] != '?') {
                    int k = 1;
                    while (i - k >= 0 && m[i - k][j] == '?') m[i - k++][j] = m[i][j];
                    k = 1;
                    while (i + k < r && m[i + k][j] == '?') m[i + k++][j] = m[i][j];
                }
            }
        }
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                if (m[i][j] != '?') {
                    int k = 1;
                    while (j - k >= 0 && m[i][j - k] == '?') m[i][j - k++] = m[i][j];
                    k = 1;
                    while (j + k < c && m[i][j + k] == '?') m[i][j + k++] = m[i][j];
                }
            }
        }
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j)
                printf("%c", m[i][j]);
            printf("\n");
        }
    }
    return 0;
}
