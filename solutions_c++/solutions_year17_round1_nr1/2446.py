#include<stdio.h>
#include<string.h>
#include<math.h>
#include <algorithm>
#include <queue>

char cake[26][26];
char cakeTmp[26][26];
bool firstLeter[30];
int R, C;

void solve() {
    bool solved[30], first = true;
    memcpy(cake, cakeTmp, sizeof(cake));
    memset(solved, 0x00, sizeof(solved));
    for(int i = 0; i < R; ++i)
    {
        for(int j = 0; j < C; ++j) {
            char L = cake[i][j];
            if (L == '?') continue;
            if(first && firstLeter[L - 'A']) continue;
            if(solved[L - 'A']) continue;
            solved[L - 'A'] = true;
            int iC = i, jC = j;
            int iL = i, jL = j;
            if(first) {
                firstLeter[L - 'A'] = true;
                first = false;
                i = -1;
                j = C;
            }
            bool topFind = false, leftFind = false;
            while(!topFind || !leftFind) {
                if (!topFind) {
                    if (iC - 1 >= 0 && cake[iC - 1][jC] == L)
                        --iC;
                    else
                        topFind = true;
                }
                if (!leftFind) {
                    if (jC - 1 >= 0 && cake[iC][jC - 1] == L)
                        --jC;
                    else
                        leftFind = true;
                }
            }
            while(iL + 1 < R && cake[iL + 1][jL] == L) {
                iL++;
            }
            while(jL + 1 < C && cake[iL][jL + 1] == L) {
                jL++;
            }
            bool stop = false;
            while(!stop) {
                if (iC - 1 >= 0) {
                    for (int y = jC; y <= jL; ++y) {
                        if (cake[iC - 1][y] != '?' && cake[iC - 1][y] != L) {
                            stop = true;
                            break;
                        }
                    }
                    if (!stop) {
                        --iC;
                    }
                } else {
                    stop = true;
                }
            }
            stop = false;
            while(!stop) {
                if (jC - 1 >= 0) {
                    for (int x = iC; x <= iL; ++x) {
                        if (cake[x][jC - 1] != '?' && cake[x][jC - 1] != L) {
                            stop = true;
                            break;
                        }
                    }
                    if (!stop) {
                        --jC;
                    }
                } else {
                    stop = true;
                }
            }
            stop = false;
            while(!stop) {
                if (iL + 1 < R) {
                    for (int y = jC; y <= jL; ++y) {
                        if (cake[iL + 1][y] != '?' && cake[iL + 1][y] != L) {
                            stop = true;
                            break;
                        }
                    }
                    if (!stop) {
                        ++iL;
                    }
                } else {
                    stop = true;
                }
            }
            stop = false;
            while(!stop) {
                if (jL + 1 < C) {
                    for (int x = iC; x <= iL; ++x) {
                        if (cake[x][jL + 1] != '?' && cake[x][jL + 1] != L) {
                            stop = true;
                            break;
                        }
                    }
                    if (!stop) {
                        ++jL;
                    }
                } else {
                    stop = true;
                }
            }
            for(int x = iC; x <= iL; ++x)
                for(int y = jC; y <= jL; ++y)
                    cake[x][y] = L;
        }
    }

    for(int i = 0; i < R; ++i)
    {
        for(int j = 0; j < C; ++j) {
            if (cake[i][j] == '?') {
                solve();
                return;
            }
        }
    }
}

int main() {
    int T;
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "r", stdin);
    scanf("%d", &T);
    for(int i = 0; i < T;++i) {
        scanf("%d %d", &R, &C);
        memset(cake, 0x00, sizeof(cake));
        for(int i = 0; i < R; ++i)
            scanf("%s", cake[i]);
        memcpy(cakeTmp, cake, sizeof(cake));
        memset(firstLeter, 0x00, sizeof(firstLeter));
        solve();
        printf("Case #%d:\n", i+1);
        for(int i = 0; i < R; ++i)
            printf("%s\n", cake[i]);
    }

    return 0;
}
