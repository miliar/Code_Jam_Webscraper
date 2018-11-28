#include <cstdio>
#include <cstring>
using namespace std;

int R, C;
char cake[30][30];

void write_up(int r, int c, char ch) {
    for(int i=r; cake[i][c]; --i)
        if( cake[i][c] == '?' )
            cake[i][c] = ch;
        else break;
}

void write_down(int r, int c, char ch) {
    for(int i=r; cake[i][c]; ++i)
        if( cake[i][c] == '?' )
            cake[i][c] = ch;
        else break;
}

void write_left(int r, int c, char ch) {
    for(int j=c; cake[r][j]; --j)
        if( cake[r][j] == '?' )
            cake[r][j] = ch;
        else break;
}

void write_right(int r, int c, char ch) {
    for(int j=c; cake[r][j]; ++j)
        if( cake[r][j] == '?' )
            cake[r][j] = ch;
        else break;
}

int main() {
    int T;
    scanf("%d", &T);
    for(int NCASE=1; NCASE<=T; ++NCASE) {
        memset(cake, 0, sizeof(cake));
        scanf("%d%d", &R, &C);
        for(int i=1; i<=R; ++i)
            scanf("%s", cake[i]+1);
        for(int i=1; i<=R; ++i)
            for(int j=1; j<=C; ++j)
                if( cake[i][j] != '?' )
                    write_up(i-1, j, cake[i][j]);
        for(int i=1; i<=R; ++i)
            for(int j=1; j<=C; ++j)
                if( cake[i][j] != '?' )
                    write_down(i+1, j, cake[i][j]);
        for(int j=1; j<=C; ++j)
            for(int i=1; i<=R; ++i)
                if( cake[i][j] != '?' )
                    write_left(i, j-1, cake[i][j]);
        for(int j=1; j<=C; ++j)
            for(int i=1; i<=R; ++i)
                if( cake[i][j] != '?' )
                    write_right(i, j+1, cake[i][j]);
        printf("Case #%d:\n", NCASE);
        for(int i=1; i<=R; ++i)
            puts(cake[i] + 1);
    }
}
