#include <bits/stdc++.h>
using namespace std;

char grid[50][50];

int main () {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t; cin >> t;
    for (int cas = 1; cas <= t; cas++) {
        int r,c;
        cin >> r >> c;

        for (int i=1; i<=r; i++) {
            for (int j=1; j<=c; j++) {
                cin >> grid[i][j];
            }
        }

        for (int i=1; i<=r; i++) {
            for (int j=1; j<=c; j++) {
                if ( grid[i][j] != '?' ) {

                    for (int j2 = j+1; j2<=c; j2++) {
                        if ( grid[i][j2] != '?' ) break;
                        grid[i][j2] = grid[i][j];
                    }

                    for (int j2 = j-1; j2>=1; j2--) {
                        if ( grid[i][j2] != '?' ) break;
                        grid[i][j2] = grid[i][j];
                    }
                }
            }
        }

        for (int i=2; i<=r; i++) {
            for (int j=1; j<=c; j++) {
                if ( grid[i][j] == '?' ) grid[i][j] = grid[i-1][j];
            }
        }

        for (int i=r-1; i>=1; i--) {
            for (int j=1; j<=c; j++) {
                if ( grid[i][j] == '?' ) grid[i][j] = grid[i+1][j];
            }
        }


        cout << "Case #" << cas << ":" << endl;
        for (int i=1; i<=r; i++) {
            for (int j=1; j<=c; j++) {
                cout << grid[i][j];
            }
            cout << endl;
        }
    }
}
