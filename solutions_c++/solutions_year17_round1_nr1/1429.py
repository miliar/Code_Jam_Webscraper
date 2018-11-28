#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int r, c;
        cin >> r >> c;
        vector<string> grid(r);
        for (int i = 0; i < r; i++) {
            cin >> grid[i];
        }
        for (int i = 0; i < r; i++) {
            char letter = 0;
            for (int j = 0; j < c; j++) {
                if (grid[i][j] != '?') {
                    letter = grid[i][j];
                    break;
                }
            }
            if (letter) {
                for (int j = 0; j < c; j++) {
                    if (grid[i][j] == '?') {
                        grid[i][j] = letter;
                    } else {
                        letter = grid[i][j];
                    }
                }
            }
        }
        string line;
        for (int i = 0; i < r; i++) {
            if (grid[i][0] != '?') {
                line = grid[i];
                break;
            }
        }
        for (int i = 0; i < r; i++) {
            if (grid[i][0] == '?') {
                grid[i] = line;
            } else {
                line = grid[i];
            }
        }
        cout << "Case #" << t << ":" << endl;
        for (int i = 0; i < r; i++) {
            cout << grid[i] << endl;
        }
    }
}
