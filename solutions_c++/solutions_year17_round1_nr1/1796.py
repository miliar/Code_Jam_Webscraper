#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

char cell[25][26];

int main(int argc, char **argv)
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        printf("Case #%d:\n", t);

        int R,C;
        scanf("%d %d\n", &R, &C);

        for (int r = 0; r != R; r++) {
            gets(cell[r]);
        }

        for (int r = 0; r != R; r++) {
            int first_char = 0;
            while (cell[r][first_char] == '?')
                first_char++;

            if (first_char == C)
                continue;

            for (int i = 0; i != first_char; i++)
                cell[r][i] = cell[r][first_char];

            for (int i = first_char+1; i != C; i++)
                if (cell[r][i] == '?')
                    cell[r][i] = cell[r][i-1];
        }

        int num_first_empty_row = 0;
        for (int r = 0; r != R; r++) {
            int first_char = 0;
            while (cell[r][first_char] == '?')
                first_char++;

            if (first_char == 0)
                break;

            num_first_empty_row++;
        }

        for (int r = num_first_empty_row-1; r >= 0; r--) {
            for (int c = 0; c != C; c++)
                cell[r][c] = cell[r+1][c];
        }


        for (int r = 1; r != R; r++) {
            int first_char = 0;
            while (cell[r][first_char] == '?')
                first_char++;

            if (first_char == 0)
                continue;

            for (int c = 0; c != C; c++)
                cell[r][c] = cell[r-1][c];
        }

        for (int r = 0; r != R; r++) {
            for (int c = 0; c != C; c++)
                printf("%c", cell[r][c]);

            printf("\n");
        }
    }
	return 0;
}
