#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++) {
        int n, m;
        scanf("%d%d", &n, &m);
        char maze[30][30];
        gets(maze[0]);
        for (int i = 0; i < n; i++) {
            gets(maze[i]);
        }
        bool used[26];
        memset(used, false, sizeof(used));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++)
            if (maze[j][i] != '?' && !used[maze[j][i] - 'A']) {
                used[maze[j][i] - 'A'] = true;
                for (int k = j - 1; k >= 0; k--) {
                    if (maze[k][i] == '?') {
                        maze[k][i] = maze[j][i];
                    } else {
                        break;
                    }
                }
                for (int k = j + 1; k < n; k++) {
                    if (maze[k][i] == '?') {
                        maze[k][i] = maze[j][i];
                    } else {
                        break;
                    }
                }
            }
            if (maze[0][i] == '?' && i > 0 && maze[0][i - 1] != '?') {
                for (int j = 0; j < n; j++) {
                    maze[j][i] = maze[j][i - 1];
                }
            }
        }
        for (int i = m - 1; i > 0; i--)
        if (maze[0][i] != '?' && maze[0][i - 1] == '?') {
            for (int j = 0; j < n; j++) {
                maze[j][i - 1] = maze[j][i];
            }
        }
        printf("Case #%d:\n",t);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) printf("%c", maze[i][j]);
            printf("\n");
        }
    }
    return 0;
}
