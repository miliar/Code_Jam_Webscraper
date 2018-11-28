#include <iostream>
using namespace std;

void go() {
    int n;
    cin >> n;
    bool grid[110][110];
    bool cross[110][110];
    bool mod[110][110];
    bool row[110];
    bool col[110];
    bool diag1[210];
    bool diag2[210];
    memset(grid, 0, sizeof(grid));
    memset(cross, 0, sizeof(cross));
    memset(mod, 0, sizeof(mod));
    memset(row, 0, sizeof(row));
    memset(col, 0, sizeof(col));
    memset(diag1, 0, sizeof(diag1));
    memset(diag2, 0, sizeof(diag2));

    int m;
    cin >> m;
    for (int i = 0; i < m; i++) {
        char c;
        int x, y;
        cin >> c >> x >> y;
        x--; y--;
        if (c =='x' || c == 'o') {
            grid[x][y] = 1;
            row[x] = 1;
            col[y] = 1;
        }
        if (c == '+' || c == 'o') {
            cross[x][y] = 1;
            diag1[x+y] = 1;
            diag2[x-y+100] = 1;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 0 && row[i] == 0 && col[j] == 0) {
                grid[i][j] = 1;
                row[i] = 1;
                col[j] = 1;
                mod[i][j] = 1;
            }
        }
    }
    for (int k = 0; k < n; k++) {
        for (int j = 0; j <= k; j++) {
            {
                int i = k-j;
                if (cross[i][j] == 0 && diag1[i+j] == 0 && diag2[i-j+100] == 0) {
                    cross[i][j] = 1;
                    diag1[i+j] = 1;
                    diag2[i-j+100] = 1;
                    mod[i][j] = 1;
                }
            }
            {
                j = (n-1)-j;
                int i = (2*n-2-k)-j;
                if (cross[i][j] == 0 && diag1[i+j] == 0 && diag2[i-j+100] == 0) {
                    cross[i][j] = 1;
                    diag1[i+j] = 1;
                    diag2[i-j+100] = 1;
                    mod[i][j] = 1;
                }
                j = (n-1)-j;
            }
        }
    }
    int ans = 0;
    int c = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (mod[i][j]) {
                c++;
            }
            ans += grid[i][j];
            ans += cross[i][j];
        }
    }
    // cout << endl;
    // for (int i = 0; i < n; i++) {
    //     for (int j = 0; j < n; j++) {
    //         cout << ((grid[i][j] && cross[i][j]) ? 'o' : (grid[i][j] ? 'x' : (cross[i][j] ? '+' : '.')));
    //     }
    //     cout << endl;
    // }
    cout << ans << ' ' << c << '\n';
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (mod[i][j]) {
                cout << ((grid[i][j] && cross[i][j]) ? 'o' : (grid[i][j] ? 'x' : '+'));
                cout << ' ' << (i+1) << ' ' << (j+1) << '\n';
            }
        }
    }
}

int main() {
    int testn;
    cin >> testn;
    for (int testi = 0; testi < testn; testi++) {
        cout << "Case #" << testi+1 << ": ";
        go();
    }
}