#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

char mat[100][100];
int r, c;
char get(char* a)
{
    for (int i = 0; a[i]; ++i) {
        if(a[i] != '?') return a[i];
    }
    return '?';
}
char solve(int i, int j)
{
    if(i + 1>= r) return '?';
    if(mat[i+1][j] != '?') {
        return mat[i][j] = mat[i+1][j];
    } else {
        return mat[i][j] = solve(i+1, j);
    }
}
char solve2(int i, int j)
{
    if(mat[i-1][j] != '?') {
        return mat[i][j] = mat[i-1][j];
    } else {
        return mat[i][j] = solve(i-1, j);
    }
}
int main()
{
    int T;cin>>T;
    for(int TT = 1; TT <= T; ++TT) {
        printf("Case #%d:\n", TT);
        cin>>r>>c;
        for (int i = 0; i < r; ++i) {
            cin>>mat[i];
            char fill = get(mat[i]);
            if(fill == '?') continue;
            for(int j = 0; j < c; ++j) {
                if(mat[i][j] == '?') mat[i][j] = fill;
                else fill = mat[i][j];
            }
        }
        for (int i = 0; i < r; ++i) {
            if(mat[i][0] != '?') continue;
            for(int j = 0; j < c; ++j) {
                if(solve(i, j) == '?'){
                    solve2(i, j);
                }
            }
        }
        for (int i = 0; i < r; ++i) {
            for(int j = 0; j < c; ++j) {
                printf("%c", mat[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}