#include <bits/stdc++.h>
using namespace std;


int t, n, m;
char c[30][30];
int main() {
    scanf("%d", &t);
    int cs = 0;
    while (t--) {
        cs++;
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++) {
            scanf("%s", c[i]);
        }
        for (int i = 0; i < n; i++) {
            vector <int> positions;
            for (int j = 0; j < m; j++) {
                if (c[i][j] != '?') {
                    positions.push_back(j);
                }
            }
            if (positions.size() == 0) {
                continue;
            }
            positions.push_back(m);
            for (int l = 0; l < positions[0]; l++) {
                c[i][l] = c[i][positions[0]];
            }
            for (int k = 0; k < positions.size() - 1; k++) {
                for (int l = positions[k]; l < positions[k + 1]; l++) {
                    c[i][l] = c[i][positions[k]];
                }
            }
        }
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (c[i][j] == '?' && c[i - 1][j] != '?') {
                    c[i][j] = c[i - 1][j];
                }
            }
        }
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < m; j++) {
                if (c[i][j] == '?' && c[i + 1][j] != '?') {
                    c[i][j] = c[i + 1][j];
                }
            }
        }
        printf("Case #%d:\n", cs);
        for (int i = 0; i < n; i++) {
            printf("%s\n", c[i]);
        }
    }
}
