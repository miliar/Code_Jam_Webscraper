#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        cout << "Case #" << c << ": " << endl;

        int R, C;
        cin >> R >> C;
        vector<string> grid(R);
        for (int i = 0; i < R; i++)
            cin >> grid[i];

        for (int i = 0; i < R; i++) {
            char cchar = '?';
            for (int j = 0; j < C; j++) {
                if (grid[i][j] != '?') {
                    if (cchar == '?') {
                        for (int k = j-1; k >= 0 && grid[i][k] == '?'; k--)
                            grid[i][k] = grid[i][j];
                    }
                    cchar = grid[i][j];
                }
                grid[i][j] = cchar;
            }
        }

        bool changed = true;
        while (changed) {
            changed = false;
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (grid[i][j] != '?') continue;
                    if (i < R-1 && grid[i+1][j] != '?') {
                        grid[i][j] = grid[i+1][j];
                        changed = true;
                    }
                    else if (i > 0 && grid[i-1][j] != '?') {
                        grid[i][j] = grid[i-1][j];
                        changed = true;
                    }
                }
            }
        }

        for (int i = 0; i < R; i++)
            cout << grid[i] << endl;
    }
    return 0;
}
