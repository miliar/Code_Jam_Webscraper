#include <bits/stdc++.h>

const int N = 33;
char G[N][N];

int main() {
    int T; std::cin >> T;
    for (int ca = 1; ca <= T; ++ ca) {
        int r, c; std::cin >> r >> c;
        for (int i = 0; i < r; ++ i) {
            std::cin >> G[i];
            for (int j = 0; j < c; ++ j) if (G[i][j] != '?') {
                for (int k = j - 1; k >= 0 && G[i][k] == '?'; -- k)
                    G[i][k] = G[i][j];
                for (int k = j + 1; k < c && G[i][k] == '?'; ++ k)
                    G[i][k] = G[i][j];
            }
        }

        for (int i = 0; i < r; ++ i) if (G[i][0] != '?') {
            for (int k = i - 1; k >= 0 && G[k][0] == '?'; -- k) {
                for (int j = 0; j < c; ++ j)
                    G[k][j] = G[i][j];
            }
            for (int k = i + 1; k < r && G[k][0] == '?'; ++ k) {
                for (int j = 0; j < c; ++ j)
                    G[k][j] = G[i][j];
            }
        }

        std::cout << "Case #" << ca << ":\n";
        for (int i = 0; i < r; ++ i) {
            for (int j = 0; j < c; ++ j)
                putchar(G[i][j]);
            putchar('\n');
        }
    }
}
