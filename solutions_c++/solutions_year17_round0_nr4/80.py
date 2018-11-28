#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <thread>
#include <unistd.h>
#include <cstring>

using namespace std;


#define ll long long
#define ull unsigned long long
#define uint unsigned int
//long long
#define dot(x,y) ((ll)x[0]*y[0]+ (ll)x[1]*y[1])

#define cleararray(array) memset(array, 0, sizeof(array))

#define BISH 1
#define ROOK 2
#define ADDED 4

const char *icons = ".+xo!HXO";

char table[100][100];
int diag1[2*100];
int diag2[2*100];
int rows[100];
int cols[100];

int N, score;

#define d1(x,y) diag1[x+y]
#define d2(x,y) diag2[N-1+x-y]

void putbish(int x,int y,int added) {
    d1(x,y)=1;
    d2(x,y)=1;
    //printf("added %d xy(%d,%d) d1 %d d2 %d\n", added, x,y, x+y, N-1+x-y);
    score++;
    table[x][y] |= BISH;
    if (added)
        table[x][y] |= ADDED;
}

void putrook(int x,int y,int added) {
    rows[y] = 1;
    cols[x] = 1;
    table[x][y] |= ROOK;
    score++;
    if (added)
        table[x][y] |= ADDED;
}

void check_diagonal(int x, int y, int len) {
    for (int cell = 0; cell <= len; cell++) {
        //printf("try xy %d,%d\n", x,y);
        if(!d1(x,y) && !d2(x,y))
            putbish(x,y,true);
        x--;
        y++;
    }
}

void nbishops() {
    // Approach the center from two opposite corners
    int x1 = 0, y1 = 0;
    int x2 = N-1, y2 = N-1;

    for (int dd = 0; dd < N; dd++) {
        x1 = dd;
        y1 = 0;
        x2 = N-1;
        y2 = N-1 - dd;
        check_diagonal(x2, y2, dd);
        check_diagonal(x1, y1, dd);
    }
}

void nrooks() {
    for (int x = 0; x < N; x++) {
        for (int y = 0; y < N; y++) {
            if(!cols[x] && !rows[y])
                putrook(x,y,true);
        }
    }
}

int main() {
    int T;
    cin >> T;

    for (int testcase = 1; testcase <= T; testcase++) {
        int M;
        cin >> N >> M;
        score = 0;

        cleararray(table);
        cleararray(diag1);
        cleararray(diag2);
        cleararray(rows);
        cleararray(cols);

        for (int idx = 0; idx < M; idx++) {
            char type;
            int R, C;
            cin >> type >> R >> C;
            if (type == '+' || type == 'o')
                putbish(C-1, R-1,false);
            if (type == 'x' || type == 'o')
                putrook(C-1, R-1,false);
        }

        nbishops();
        nrooks();

        int numadded=0;
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                if (table[x][y] & ADDED)
                    numadded++;
            }
        }

        printf("Case #%d: %d %d\n", testcase, score, numadded);

        // for (int x = 0; x < N; x++) {
        //     for (int y = 0; y < N; y++) {
        //         printf("%c", icons[table[y][x]]);
        //     }
        //     printf("\n");
        // }

        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                if (table[x][y] & ADDED) {
                    if (table[x][y] == ROOK + BISH + ADDED)
                        printf("o %d %d\n", y+1, x+1);
                    else if (table[x][y] == ROOK + ADDED)
                        printf("x %d %d\n", y+1, x+1);
                    else if (table[x][y] == BISH + ADDED)
                        printf("+ %d %d\n", y+1, x+1);
                    else
                        abort();
                }
            }
        }

    }
    return 0;
}
