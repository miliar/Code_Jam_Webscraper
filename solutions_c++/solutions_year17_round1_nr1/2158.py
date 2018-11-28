#include <iostream>
#include <string>
#include <cstring>
using namespace std;

string cake[30];
bool used[30][30];

bool test(char p1, char p2) {
    return p1 == p2 || p2 == '?';
}

int main() {
    int t;
    cin >> t;
    for (int no = 1; no <= t; no++) {
        int row, col;
        cin >> row >> col;

        for (int r = 0; r < row; r++) {
            cin >> cake[r];
        }

        /*
        if (no == 49) {
            cout << "debug" << endl;
            for (int r = 0; r < row; r++) {
                cout << cake[r] << endl;
            }
        }
        */

        memset(used, false, sizeof(used));
        for (int c = 0; c < col; c++) {
            for (int r = 0; r < row; r++) {
                if (used[r][c] || cake[r][c] == '?') continue;

                used[r][c] = true;

                int top_r = r,
                    bot_r = r;
                while (top_r - 1 >= 0 && test(cake[r][c], cake[top_r - 1][c]) && !used[top_r - 1][c]) {
                    top_r--;
                    cake[top_r][c] = cake[r][c];
                    used[top_r][c] = true;
                }
                while (bot_r + 1 < row && test(cake[r][c], cake[bot_r + 1][c]) && !used[bot_r + 1][c]) {
                    bot_r++;
                    cake[bot_r][c] = cake[r][c];
                    used[bot_r][c] = true;
                }

                bool valid = true;
                for (int nc = c + 1; c < col; nc++) {
                    for (int nr = top_r; nr <= bot_r; nr++) {
                        if (used[nr][nc] || !test(cake[r][c], cake[nr][nc])) {
                            valid = false;
                            break;
                        }
                    }

                    if (!valid) break;

                    // 塗る
                    for (int nr = top_r; nr <= bot_r; nr++) {
                        cake[nr][nc] = cake[r][c];
                        used[nr][nc] = true;
                    }
                }
                valid = true;
                for (int nc = c - 1; c >= 0; nc--) {
                    for (int nr = top_r; nr <= bot_r; nr++) {
                        if (used[nr][nc] || !test(cake[r][c], cake[nr][nc])) {
                            valid = false;
                            break;
                        }
                    }

                    if (!valid) break;

                    // 塗る
                    for (int nr = top_r; nr <= bot_r; nr++) {
                        cake[nr][nc] = cake[r][c];
                        used[nr][nc] = true;
                    }
                }
            }
        }

        cout << "Case #" << no << ":" << endl;
        for (int r = 0; r < row; r++) {
            cout << cake[r] << endl;
        }

        /*
        if (no == 99) {
            int x, y;
            while (cin >> x >> y, x >= 0 && y >= 0) {
                cout << "used: " << used[x][y] << endl;
            }
        }
        */
    }
    return 0;
}
