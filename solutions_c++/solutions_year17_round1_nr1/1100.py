#include <bits/stdc++.h>

int R, C;
char gr[25][25];

char get(int r, int c) {
    if (r < 0 || c < 0 || r >= R || c >= C) {
        return '|';
    }
    return gr[r][c];
}

void print() {
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            printf("%c", get(r, c));
        }
        printf("\n");
    }
}

int main() {
    int T;
    scanf("%i\n", &T);
    for (int t = 0; t < T; t++) {
        printf("Case #%i:\n", t+1);
        scanf("%i %i\n", &R, &C);
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                scanf(" %c", &gr[r][c]);
            }
        }
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (get(r, c+1) == '?' && get(r, c) != '?') {
                    gr[r][c+1] = get(r, c);
                }
            }
        }

        for (int r = 0; r < (R-1); r++) {
            int c = 0;
            while (c < C) {
                int end = c+1;
                while (get(r, c) == get(r, end)) end++;

                bool good = true;
                for (int j = c; j < end; j++) {
                    if (get(r+1, j) != '?') {
                        good = false;
                    }
                }

                if (good) {
                    for (int j = c; j < end; j++) {
                        gr[r+1][j] = gr[r][j];
                    }
                }

                c = end;
            }
        }

        for (int r = R-1; r >= 0; r--) {
            for (int c = C-1; c >= 0; c--) {
                if (get(r, c-1) == '?' && get(r, c) != '?') {
                    gr[r][c-1] = get(r, c);
                }
            }
        }

        for (int r = (R-1); r >= 1; r--) {
            int c = C-1;
            while (c >= 0) {
                int end = c-1;
                while (get(r, c) == get(r, end)) end--;

                bool good = true;
                for (int j = c; j > end; j--) {
                    if (get(r-1, j) != '?') {
                        good = false;
                    }
                }

                if (good) {
                    for (int j = c; j > end; j--) {
                        gr[r-1][j] = gr[r][j];
                    }
                }

                c = end;
            }
        }
        print();
    }
}
