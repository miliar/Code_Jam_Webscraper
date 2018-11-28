#include <iostream>
#include <vector>

using namespace std;

void solve(int r, int c, vector<vector<char>>& g, vector<vector<char>>& orig) {
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            char ch = orig[i][j];
            if (ch != '?') {
                //cout << i << " " << j << endl;
                int left, right;
                for (left = j - 1; left >= 0; left--) {
                    if (g[i][left] != '?') {
                        break;
                    }
                    else {
                        g[i][left] = ch;
                    }
                }
                for (right = j + 1; right < c; right++) {
                    if (g[i][right] != '?') {
                        break;
                    }
                    else {
                        g[i][right] = ch;
                    }
                }
                //cout << left << " " << right << endl;
                int upper, down;
                for (upper = i - 1; upper >= 0; upper--) {
                    bool good = true;
                    for (int j1 = left + 1; j1 < right; j1++) {
                        if (g[upper][j1] != '?') {
                            good = false;
                            break;
                        }
                    }
                    if (good) {
                         for (int j1 = left + 1; j1 < right; j1++) {
                             g[upper][j1] = ch;
                         }
                    }
                    else {
                        break;
                    }
                }
                
                for (down = i + 1; down < r; down++) {
                    bool good = true;
                    for (int j1 = left + 1; j1 < right; j1++) {
                        if (g[down][j1] != '?') {
                            good = false;
                            break;
                        }
                    }
                    if (good) {
                         for (int j1 = left + 1; j1 < right; j1++) {
                             g[down][j1] = ch;
                         }
                    }
                    else {
                        break;
                    }
                }
            }
        }
    }
    
}

int main() {
    int t;
    cin >> t;
    for (int kase = 1; kase <= t; kase++) {
        int r, c;
        cin >> r >> c;
        vector<vector<char>> grid(r, vector<char>(c));
        vector<vector<char>> orig(r, vector<char>(c));
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> grid[i][j];
                orig[i][j] = grid[i][j];
            }
        }
        solve(r, c, grid, orig);
        cout << "Case #" << kase << ":" << endl;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cout << grid[i][j];
            }
            cout << endl;
        }
    }
    return 0;  
}