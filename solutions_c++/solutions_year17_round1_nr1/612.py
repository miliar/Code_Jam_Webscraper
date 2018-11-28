#include<cstdio>
using namespace std;

int R, C;
char cakes[30][30];
int num;
int place_x[200];
int place_y[200];

void greedy(int x, int y) {
    char t = cakes[x][y];
    int left, right, top, bottom; // –¼‘OŠÔˆá‚¦‚½
    int i, j;
    for(i = x-1; i >= 0; --i) {
        if(cakes[i][y] != '?') {
            break;
        }
    }
    left = i+1;
    for(j = y-1; j >= 0; --j) {
        if(cakes[left][j] != '?') {
            break;
        }
    }
    top = j+1;

    for(i = left; i <= x; ++i) {
        for(j = top; j <= y; ++j) {
            if(cakes[i][j] != '?' && cakes[i][j] != t) {
                fprintf(stderr, "check! %d %d - %d %d - %d %d\n", x, y, left, top, i, j);
            }
        }
    }

    for(bottom = y+1; bottom < C; ++bottom) {
        int i;
        for(i = left; i <= x; ++i) {
            if(cakes[i][bottom] != '?') break;
        }
        if(i <= x) break;
    }
    for(right = x+1; right < R; ++right) {
        int j;
        for(j = top; j < bottom; ++j) {
            if(cakes[right][j] != '?') break;
        }
        if(j < bottom) break;
    }

    for(int i = left; i < right; ++i) {
        for(int j = top; j < bottom; ++j) {
            cakes[i][j] = t;
        }
    }
}

void solve() {
    for(int i = 0; i < num; ++i) {
        greedy(place_x[i], place_y[i]);
    }
}

void solve_and_print() {
    char bufs[30];
    scanf("%d %d", &R, &C);
    gets(bufs);
    num = 0;
    for(int i = 0; i < R; ++i) {
        gets(bufs);
        for(int j = 0; j < C; ++j) {
            cakes[i][j] = bufs[j];
            if(bufs[j] != '?') {
                place_x[num] = i;
                place_y[num] = j;
                ++num;
            }
        }
    }

    solve();

    for(int i = 0; i < R; ++i) {
        for(int j = 0; j < C; ++j) {
            putchar(cakes[i][j]);
            if(cakes[i][j] == '?') fprintf(stderr, "trouble!\n");
        }
        putchar('\n');
    }
}


int main() {
    int dataset_num, case_num;

    scanf("%d", &dataset_num);
    for(case_num = 1; case_num <= dataset_num; ++case_num) {
        printf("Case #%d:\n", case_num);

        solve_and_print();
    }

    return 0;
}
