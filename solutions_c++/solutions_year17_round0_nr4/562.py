#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int n;

void print_board(vector<vector<bool>> &b_l, vector<vector<bool>> b_x) {
    char ch;
    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < n; ++col) {
            bool is_l = b_l[row][col];
            bool is_x = b_x[row][col];
            if (is_l && is_x)
                ch = 'o';
            else if (is_l)
                ch = '+';
            else if (is_x)
                ch = 'x';
            else ch = '.';
            cout << ch << " ";
        }
        cout << endl;
    }
}

int main() {
    int t, m;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n >> m;
        vector<vector<bool>> b_l;
        vector<vector<bool>> b_x;
        set<pair<int, int>> changed;
        for (int j = 0; j < n; ++j) {
            b_l.push_back(vector<bool>(n, false));
            b_x.push_back(vector<bool>(n, false));
        }
        char type;
        int row, col;

        vector<bool> x_row_taken(n, false);
        vector<bool> x_col_taken(n, false);

        for (int j = 0; j < m; ++j) {
            cin >> type >> row >> col;
            row--, col--;
            if (type == 'o' || type == '+') {
                b_l[row][col] = true;
                // TODO
            }
            if (type == 'o' || type == 'x') {
                b_x[row][col] = true;
                x_row_taken[row] = x_col_taken[col] = true;
            }
        }

//        cout << "BEFORE:" << endl;
//        print_board(b_l, b_x);

        // fill diagonal type (x)
        row = col = 0;
        for (row = 0; row < n; ++row) {
            if (x_row_taken[row]) continue;
            for (; col < n; ++col) {
                if (!x_col_taken[col]) break;
            }
            if (col == n) break;
            b_x[row][col] = true;
            x_row_taken[row] = x_col_taken[col] = true;
            changed.insert(make_pair(row, col));
        }

        // fill the top row with +
        // (this is only a valid solution for the small dataset)
        row = 0;
        for (col = 0; col < n; ++col) {
            if (!b_l[row][col]) {
                b_l[row][col] = true;
                changed.insert(make_pair(row, col));
            }
        }
        row = n-1;
        for (col = 1; col < n -1; ++col) {
            if (!b_l[row][col]) {
                b_l[row][col] = true;
                changed.insert(make_pair(row, col));
            }
        }

        int style_points_total = 3*n - 2;
        if (n == 1) style_points_total += 1;

        // output solution
        cout << "Case #" << i << ": " << style_points_total << " " << changed.size() << "\n";
        char ch;
        for (const pair<int, int> &p : changed) {
            bool is_l = b_l[p.first][p.second];
            bool is_x = b_x[p.first][p.second];
            if (is_l && is_x)
                ch = 'o';
            else if (is_l)
                ch = '+';
            else
                ch = 'x';
            cout << ch << " " << p.first + 1 << " " << p.second + 1 << "\n";
        }

//        cout << "\nAFTER:" <<endl;
//        print_board(b_l, b_x);
//        cout << "\n\n\n";
    }
    return 0;
}