#include <bits/stdc++.h>
using namespace std;
const int maxr = 30;

int r, c;
string grid[maxr];

int count(int r1, int c1, int r2, int c2) {
    int tot = 0;
    for (int i = r1; i < r2; i++) {
        for (int j = c1; j < c2; j++) {
            if (grid[i][j] != '?') {
                ++tot;
            }
        }
    }
    return tot;
}

void go(int r1, int c1, int r2, int c2) {
    int tot = count(r1, c1, r2, c2);
    if (tot == 1) {
        char c = '!';
        for (int i = r1; i < r2; i++) {
            for (int j = c1; j < c2; j++) {
                if (grid[i][j] != '?') {
                    c = grid[i][j];
                }
            }
        }
        for (int i = r1; i < r2; i++) {
            for (int j = c1; j < c2; j++) {
                grid[i][j] = c;
            }
        }
        return;
    }

    for (int i = r1; i < r2; i++) {
        int cur = count(r1, c1, i + 1, c2);
        if (0 < cur && cur < tot) {
            go(r1, c1, i + 1, c2);
            go(i + 1, c1, r2, c2);
            return;
        }
    }

    for (int i = c1; i < c2; i++) {
        int cur = count(r1, c1, r2, i + 1);
        if (0 < cur && cur < tot) {
            go(r1, c1, r2, i + 1);
            go(r1, i + 1, r2, c2);
            return;
        }
    }
}

void solve() {
    cin >> r >> c;
    for (int i = 0; i < r; i++) {
        cin >> grid[i];
    }

    go(0, 0, r, c);

    for (int i = 0; i < r; i++) {
        cout << grid[i] << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int numCases;
    cin >> numCases;
    for (int i = 1; i <= numCases; i++) {
        cout << "Case #" << i << ": " << '\n';
        solve();
        cerr << i << endl;
    }
    return 0;
}
