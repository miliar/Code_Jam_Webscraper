#include<bits/stdc++.h>
using namespace std;

int main() {
    int tc;
    cin >> tc;
    for(int t = 1; t <= tc; ++t) {
        int n, m;
        char grid[30][30];
        for(int i = 0; i < 30; ++i) for(int j = 0; j < 30; ++j) grid[i][j] = 0;
        cin >> n >> m;
        string str;
        for(int i = 1; i <= n; ++i) {
            cin >> str;
            for(int j = 1; j <= str.length(); ++j) {
                grid[i][j] = str[j - 1];
            }
        }
        int i, j, k;
        for(i = 1; i <= n; ++i) {
            for(j = 2; j <= m; ++j) {
                //printf("%c ", grid[i][j]);
                if(grid[i][j] == '?') {
                    grid[i][j] = grid[i][j-1];
                }
            }
            for(j = m-1; j >= 1; --j) {
                //printf("%c ", grid[i][j]);
                if(grid[i][j] == '?') {
                    grid[i][j] = grid[i][j+1];
                }
            }
        }
        for(i = 1; i <= m; ++i) {
            for(j = 2; j <= n; ++j) {
                if(grid[j][i] == '?') {
                    grid[j][i] = grid[j-1][i];
                }
            }
            for(j = n-1; j >= 1; --j) {
                if(grid[j][i] == '?') {
                    grid[j][i] = grid[j+1][i];
                }
            }
        }
        cout << "Case #" << t << ":" << endl;
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= m; ++j) {
                cout << grid[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}
