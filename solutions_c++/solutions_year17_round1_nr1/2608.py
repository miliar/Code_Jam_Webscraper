#include <iostream>

using namespace std;

int main() {
    int t, r, c;
    char grid[25][25];
    bool empty[25];
    int leftmost[25];
    int first;
    cin >> t;

    for (int n = 1; n <= t; n++) {
        first = -1;
        cin >> r >> c;
        for (int i = 0; i < r; i++) {
            empty[i] = true;
            leftmost[i] = -1;
            for (int j = 0; j < c; j++) {
                cin >> grid[i][j];
                if (grid[i][j] != '?') {
                    if (empty[i]) {
                        empty[i] = false;
                        if (first == -1) {
                            first = i;
                        }
                    }
                    if (leftmost[i] == -1) {
                        leftmost[i] = j;
                    }
                }
            }
        }

        for (int i = first; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (grid[i][j] == '?') {
                    if (empty[i]) {
                        grid[i][j] = grid[i-1][j];
                    }
                    else if (j == 0) {
                        grid[i][j] = grid[i][leftmost[i]];
                    }
                    else {
                        grid[i][j] = grid[i][j-1];
                    }
                }
            }
        }

        for (int i = first - 1; i >= 0; i--) {
            for (int j = 0; j < c; j++) {
                grid[i][j] = grid[i+1][j];
            }
        }

        cout << "Case #" << n << ":" << endl;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cout << grid[i][j];
            }
            cout << endl;
        }
    }
}
