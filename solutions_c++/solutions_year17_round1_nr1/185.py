#include <bits/stdc++.h>

using namespace std;
int t, r, c;
char grid[30][30];
int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> r >> c;
        for (int y = 0; y < r; y++) {
            for (int x = 0; x < c; x++) {
                cin >> grid[y][x];
            }
        }

        // cout << "Case #" << test << ":" << endl;
        // for (int y = 0; y < r; y++) {
        //     for (int x = 0; x < c; x++) {
        //         cout << grid[y][x];
        //     }
        //     cout << endl;
        // }

        char cur = 0;
        for (int y = 0; y < r; y++) {
            for (int x = 0; x < c; x++) {
                if (grid[y][x] != '?') {
                    if (cur == 0) {
                        for (int lastx = x - 1; lastx >= 0; lastx--) {
                            if (grid[y][0] != '?' && grid[y][0] != 0) break;
                            grid[y][lastx] = grid[y][x];
                        }
                    }
                    cur = grid[y][x];
                }
                grid[y][x] = cur;
                // cout << grid[y][x];
            }
            cur = 0;
        }

        // cout << "Case #" << test << ":" << endl;
        // for (int y = 0; y < r; y++) {
        //     for (int x = 0; x < c; x++) {
        //         cout << grid[y][x];
        //     }
        //     cout << endl;
        // }

        for (int y = 0; y < r - 1; y++) {
            if (grid[y][0] != '?' && grid[y][0] != 0) continue;
            for (int x = 0; x < c; x++) {
                for (int y2 = y + 1; y2 < r; y2++) {
                    if (grid[y2][x] != '?' && grid[y2][x] != 0) {
                        grid[y][x] = grid[y2][x];
                        break;
                    }
                }
            }
        }

        for (int y = r - 1; y >= 1; y--) {
            if (grid[y][0] != '?' && grid[y][0] != 0) continue;
            for (int x = 0; x < c; x++) {
                for (int y2 = y - 1; y2 >= 0; y2--) {
                    if (grid[y2][x] != '?' && grid[y2][x] != 0) {
                        grid[y][x] = grid[y2][x];
                        break;
                    }
                }
            }
        }

        cout << "Case #" << test << ": " << endl;
        for (int y = 0; y < r; y++) {
            for (int x = 0; x < c; x++) {
                cout << grid[y][x];
            }
            cout << endl;
        }
    }

    
}