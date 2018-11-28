#include <bits/stdc++.h>

using namespace std;

#define pii pair < int, int >

int t, r, c;
char grid[30][30];

int main() {
    scanf("%d", &t);
    for (int tc = 0; tc < t; tc++) {
        for (int i = 0; i < 30; i++)
            for (int j = 0; j < 30; j++)
                grid[i][j] = '.';

        scanf("%d %d", &r, &c);
        for (int i = 1; i <= r; i++)
            for (int j = 1; j <= c; j++)
                cin >> grid[i][j];

        for (char ch = 'A'; ch <= 'Z'; ch++) {
            int min_x = 100000, max_x = 0, min_y = 100000, max_y = 0, cont = 0;
            for (int i = 1; i <= r; i++)
                for (int j = 1; j <= c; j++)
                    if (grid[i][j] == ch) {
                        min_x = min(min_x, i); max_x = max(max_x, i);
                        min_y = min(min_y, j); max_y = max(max_y, j);
                        cont++;
                    }

            if (cont > 0) {
                while (1) {
                    bool a = true, b = true, e = true, f = true;
                    for (int i = min_x; i <= max_x; i++)
                        if (grid[i][min_y-1] != '?')
                            a = false;
                    for (int i = min_x; i <= max_x; i++)
                        if (grid[i][max_y+1] != '?')
                            b = false;
                    for (int i = min_y; i <= max_y; i++)
                        if (grid[min_x-1][i] != '?')
                            e = false;
                    for (int i = min_y; i <= max_y; i++)
                        if (grid[max_x+1][i] != '?')
                            f = false;

                    if (!a && !b && !e && !f) break;

                    if (a) min_y--;
                    else if (b) max_y++;
                    else if (e) min_x--;
                    else max_x++;
                }

                for (int i = min_x; i <= max_x; i++)
                    for (int j = min_y; j <= max_y; j++)
                        grid[i][j] = ch;
            }
        }


        printf("Case #%d:\n", tc+1);
        for (int i = 1; i <= r; i++) {
            for (int j = 1; j <= c; j++)
                printf("%c", grid[i][j]);
            printf("\n");
        }
    }

    return 0;
}
