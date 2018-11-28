#include <cstdio>

int main(void) {
    int T, R, C, dis1, dis2;
    char t1, t2;
    char cake[30][30];

    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas) {
        scanf("%d %d", &R, &C);

        for(int r = 0; r < R; ++r) {
            scanf("%s", cake[r]);
        }


        for(int r = 0; r < R; ++r) {
            for(int c = 0; c < C; ++c) {
                if(cake[r][c] == '?') {
                    dis1 = dis2 = 1e9;
                    t1 = t2 = '?';
                    for(int i = r-1; i >= 0; --i) {
                        if(cake[i][c] != '?') {
                            t1 = cake[i][c];
                            dis1 = r-i;
                            break;
                        }
                    }
                    for(int i = r+1; i < R; ++i) {
                        if(cake[i][c] != '?') {
                            t2 = cake[i][c];
                            dis2 = i-r;
                            break;
                        }
                    }
                    if(dis1 <= dis2) {
                        cake[r][c] = t1;
                    }
                    else {
                        cake[r][c] = t2;
                    }
                }
            }
        }

        for(int r = 0; r < R; ++r) {
            for(int c = 0; c < C; ++c) {
                if(cake[r][c] == '?') {
                    dis1 = dis2 = 1e9;
                    t1 = t2 = '?';
                    for(int i = c-1; i >= 0; --i) {
                        if(cake[r][i] != '?') {
                            t1 = cake[r][i];
                            dis1 = c-i;
                            break;
                        }
                    }
                    for(int i = c+1; i < C; ++i) {
                        if(cake[r][i] != '?') {
                            t2 = cake[r][i];
                            dis2 = i-c;
                            break;
                        }
                    }
                    if(dis1 <= dis2) {
                        cake[r][c] = t1;
                    }
                    else {
                        cake[r][c] = t2;
                    }
                }
            }
        }

        printf("Case #%d:\n", cas);
        for(int r = 0; r < R; ++r) {
            for(int c = 0; c < C; ++c) {
                printf("%c", cake[r][c]);
            }
            printf("\n");
        }

    }


    return 0;
}
