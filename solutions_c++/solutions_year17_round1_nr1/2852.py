#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; kase++) {
        char gird[30][30];
        int r, c, used[30][30];
        memset(gird, 0, sizeof(gird));
        memset(used, 0, sizeof(used));
        scanf("%d %d", &r, &c);
        for (int i = 0; i < r; i++) {
                scanf("%s", gird[i]);
        }
        for (int i = 0; i < r; i++)
        	for (int j = 0; j < c; j++)
        	    if (gird[i][j] != '?') used[i][j] = 1;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (used[i][j]) {
                    for (int x = j + 1; x < c; x++) {
                        if (gird[i][x] != '?') break;
                        gird[i][x] = gird[i][j];
                    }
                    for (int x = j - 1; x >= 0; x--) {
                        if (gird[i][x] != '?') break;
                        gird[i][x] = gird[i][j];
                    }
                }
            }
        }
        //cout << "Yes" << endl;
        for (int i = 1; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (gird[i][j] == '?') {
                    gird[i][j] = gird[i - 1][j];
                }
            }
        }
        for (int i = r - 2; i >= 0; i--) {
            for (int j = 0; j < c; j++) {
                if (gird[i][j] == '?') {
                    gird[i][j] = gird[i + 1][j];
                }
            }
        }
        printf("Case #%d:\n", kase);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cout << (char)gird[i][j];
            }
            cout << endl;
        }
    }
}