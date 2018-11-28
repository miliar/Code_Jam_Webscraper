#include <bits/stdc++.h>
#define X first
#define Y second
#define FI(i, a, b) for (int i = (a); i <= (b); i++)
#define FD(i, a, b) for (int i = (a); i >= (b); i--)
using namespace std;
using LL = long long;

const int N = 30;
char g[N][N];
void work(int testCase) {
    int row, col;
    scanf("%d%d", &row, &col);
    FI(i,1,row) scanf("%s", g[i]+1);
    int lastRow = 0;
    FI(i,1,row) {
        int lastCol = 0;
        bool update = false;
        FI(j,1,col) if (g[i][j] != '?') {
            update = true;
            FI(k,lastCol+1, j) g[i][k] = g[i][j];\
            lastCol = j;
        }
        if (lastCol != 0 && lastCol != col) {
            FI(k,lastCol+1, col) g[i][k] = g[i][lastCol];
        }
        if (update) FI(k,lastRow+1,i-1) {
            FI(j,1,col) g[k][j] = g[i][j];
            lastRow = i;
        }
    }
    if (lastRow != 0 && lastRow != row) {
        FI(k,lastRow+1,row) {
            FI(j,1,col) g[k][j] = g[lastRow][j];
        }
    }
    printf("Case #%d:\n", testCase);
    FI(i,1,row) printf("%s\n", g[i]+1);
}

int main() {
    int T;
    scanf("%d", &T);
    FI(i, 1, T)
    work(i);
}