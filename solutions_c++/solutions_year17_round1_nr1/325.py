#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        int R, C;
        scanf("%d %d", &R, &C);
        vector<vector<char>> cake(R, vector<char>(C));
        for (int i = 0; i < R; i++)
            for (int j = 0; j < C; j++)
                scanf(" %c ", &cake[i][j]);
        map<char, bool> done;
        for (int i = 0; i < R; i++) 
            for (int j = 0; j < C; j++)
                if (cake[i][j] != '?' && !done[cake[i][j]]) {
                    done[cake[i][j]] = true;
                    int left = j, right = j;
                    while (left > 0 && cake[i][left - 1] == '?')
                        left--;
                    while (right < C - 1 && cake[i][right + 1] == '?')
                        right++;
                    int up = i, down = i;
                    while (up > 0) {
                        bool empty = true;
                        for (int k = left; k <= right; k++)
                            if (cake[up - 1][k] != '?') {
                                empty = false;
                                break;
                            }
                        if (!empty)
                            break;
                        else
                            up--;
                    }
                    while (down < R - 1) {
                        bool empty = true;
                        for (int k = left; k <= right; k++)
                            if (cake[down + 1][k] != '?') {
                                empty = false;
                                break;
                            }
                        if (!empty)
                            break;
                        else
                            down++;
                    }
                    for (int k = up; k <= down; k++)
                        for (int l = left; l <= right; l++)
                            cake[k][l] = cake[i][j];
                }
        printf("Case #%d:\n", tc);
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++)
                printf("%c", cake[i][j]);
            printf("\n");
        }
    }
    return 0;
}
