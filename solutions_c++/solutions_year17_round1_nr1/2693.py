#include <iostream>
#include <cstdio>

void fill (int x, int y, int r, int c);

int count (int x, int y, int r, int c);

char a[26][26];

int main(int argc, const char * argv[]) {
    int t;
    scanf("%d", &t);
    for (int k = 0; k < t; k++) {
        int r, c;
        scanf("%d %d\n", &r, &c);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                scanf("%c", &a[i][j]);
                if (a[i][j] == '?') {
                    a[i][j] = 0;
                }
            }
            scanf("\n");
        }
        fill(0, 0, r, c);
        printf("Case #%d:", k);
        for (int i = 0; i< r; i++) {
            for (int j = 0; j < c;j++) {
                printf("%c", a[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}

int count (int x, int y, int r, int c) {
    int res = 0;
    for (int i = x; i < r; i++) {
        for (int j = y; j < c; j++) {
            if (a[i][j]) {
                res++;
            }
        }
    }
    return res;
}

void fill (int x, int y, int r, int c) {
    if (count(x, y, r, c) == 1) {
        char name = '\0';
        for (int i = x; i < r; i++) {
            for (int j = y; j < c; j++) {
                if (a[i][j]) {
                    name = a[i][j];
                    break;
                }
            }
        }
        for (int i = x; i < r; i++) {
            for (int j = y; j < c; j++) {
                a[i][j] = name;
            }
        }
    }
    for (int i = x + 1; i < r; i++) {
        if (count(x, y, i, c) && count(i, y, r, c)) {
            fill(x, y, i, c);
            fill(i, y, r, c);
            return;
        }
    }
    
    for (int i = y + 1; i < c; i++) {
        if (count(x, y, r, i) && count(x, i, r, c)) {
            fill(x, y, r, i);
            fill(x, i, r, c);
            return;
        }
    }
}

