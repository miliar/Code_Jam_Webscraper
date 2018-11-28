#include <bits/stdc++.h>

using namespace std;

void solve() {
    int r, c;
    cin >> r >> c;
    vector<vector<char> > grid(r, vector<char>(c));
    vector<int> q(r, 0);

    int totalq = 0;
    for (int i = 0; i < r; ++i) {
        char lastc = 0;
        for (int j = 0; j < c; ++j) {
            cin >> grid[i][j];
            if (grid[i][j] == '?') {
                ++q[i];
                ++totalq;
            } else {
                lastc = grid[i][j];
                for (int k = j - 1; k >= 0 && grid[i][k] == '?'; --k) {
                    grid[i][k] = grid[i][j];
                    --q[i];
                    --totalq;
                }
            }
        }
        if (lastc) {
            for (int j = c - 1; j >= 0 && grid[i][j] == '?'; --j) {
                grid[i][j] = lastc;
            }
        }
    }
    for (int j = 0; j < c; ++j) {
        char lastc = 0;
        for (int i = 0; i < r; ++i) {
            if (grid[i][j] != '?') {
                lastc = grid[i][j];
                for (int k = i - 1; k >= 0 && grid[k][j] == '?'; --k) {
                    grid[k][j] = grid[i][j];
                    --totalq;
                    --q[k];
                }
            }
        }
        if (lastc) {
            for (int i = r - 1; i >= 0 && grid[i][j] == '?'; --i) {
                grid[i][j] = lastc;
            }
        }
    }
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cout<<grid[i][j];
        }
        cout<<'\n';
    }
}

int main() {
    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        cout << "Case #" << test << ":\n";
        solve();
        cerr << "Solved case " << test << '\n';
    }
    return 0;
}