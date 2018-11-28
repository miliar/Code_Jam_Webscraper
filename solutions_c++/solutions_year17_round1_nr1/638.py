#include <bits/stdc++.h>
using namespace std;

void Solve(int testNum) {
    int n, m;
    char mat[100][100];
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) scanf("%s", mat[i]);

    for(int i = 0; i < n; i++) {
        char let = '?';
        for(int j = 0; j < m; j++) {
            if(mat[i][j] != '?') {
                let = mat[i][j];
                break;
            }
        }
        for(int j = 0; j < m; j++)
            if(mat[i][j] != '?') let = mat[i][j];
            else mat[i][j] = let;
    }

    for(int j = 0; j < m; j++) {
        int let = '?';
        for(int i = 0; i < n; i++) {
            if(mat[i][j] != '?') {
                let = mat[i][j];
                break;
            }
        }
        for(int i = 0; i < n; i++) {
            if(mat[i][j] != '?') let = mat[i][j];
            else mat[i][j] = let;
        }
    }

    printf("Case #%d:\n", testNum);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) cout << mat[i][j];
        cout << endl;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++) Solve(i+1);
}
