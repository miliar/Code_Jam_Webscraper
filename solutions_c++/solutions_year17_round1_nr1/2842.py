#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cmath>

using namespace std;

int can_extend(int R, int C, const vector< vector<char> > & grid, int r_min, int r_max, int c_min, int c_max, int dir) {
    // return values correspond to up down left right
    if (dir == 1) {
        if (r_min > 0) {
            bool can_extend = true;
            for (int c = c_min; c <= c_max; c++) {
                if (grid[r_min-1][c] != '?') {
                    can_extend = false;
                    break;
                }
            }
            if (can_extend) return 1;
            else return 0;
        }
    }
    else if (dir == 2) {
        if (r_max < R-1) {
            bool can_extend = true;
            for (int c = c_min; c <= c_max; c++) {
                if (grid[r_max+1][c] != '?') {
                    can_extend = false;
                    break;
                }
            }
            if (can_extend) return 2;
            else return 0;
        }
    }
    else if (dir == 3) {
        if (c_min > 0) {
            bool can_extend = true;
            for (int r = r_min; r <= r_max; r++) {
                if (grid[r][c_min-1] != '?') {
                    can_extend = false;
                    break;
                }
            }
            if (can_extend) return 3;
            else return 0;
        }
    }
    else if (dir == 4) {
        if (c_max < C-1) {
            bool can_extend = true;
            for (int r = r_min; r <= r_max; r++) {
                if (grid[r][c_max+1] != '?') {
                    can_extend = false;
                    break;
                }
            }
            if (can_extend) return 4;
            else return 0;
        }
    }
    return 0;
}

int next_dir(int dir) {
    switch (dir) {
        case 1:
            return 4;
        case 2:
            return 3;
        case 3:
            return 1;
        case 4:
            return 2;
    }
    return 0;
}

void solve() {
    int R, C; cin >> R >> C;

    vector< pair<int, int> > start_locs;
    vector< vector<char> > cake(R);
    for (int r = 0; r < R; r++) {
        cake[r].resize(C);
        string str; cin >> str;
        for (int c = 0; c < C; c++) {
            if (str[c] != '?') {
                start_locs.push_back(make_pair(r, c));
            }
            cake[r][c] = str[c];
        }
    }

    for (int i = 0; i < start_locs.size(); i++) {
        int r_min, r_max, c_min, c_max;
        r_min = start_locs[i].first;
        c_min = start_locs[i].second;
        r_max = r_min;        
        c_max = c_min;

        char ch = cake[r_min][c_min];
    
        int dir = 1;
        int cant_update_count = 0;

        while (cant_update_count < 4) {
            cant_update_count++;
            int _dir = can_extend(R, C, cake, r_min, r_max, c_min, c_max, dir);
            if (_dir == 0) {
                dir = next_dir(dir);
                continue;
            }
            cant_update_count = 0;

            if (dir == 1) {
                for (int c = c_min; c <= c_max; c++) {
                    cake[r_min-1][c] = ch;
                }
                r_min--;
            }
            else if (dir == 2) {
                for (int c = c_min; c <= c_max; c++) {
                    cake[r_max+1][c] = ch;
                }
                r_max++;
            }
            else if (dir == 3) {
                for (int r = r_min; r <= r_max; r++) {
                    cake[r][c_min-1] = ch;
                }
                c_min--;
            }
            else if (dir == 4) {
                for (int r = r_min; r <= r_max; r++) {
                    cake[r][c_max+1] = ch;
                }
                c_max++;
            }
            dir = next_dir(dir);
        }
    }

    for (int r = 0; r < R; r++) {
        cout << endl;
        for (int c = 0; c < C; c++) {
            cout << cake[r][c];
        }
    }
}

int main (void) {
    int T; cin >> T;

    for (int t = 1; t <= T; t++) {
        if (t > 1) cout << endl;
        cout << "Case #" << t << ":";
        solve();
    }

    return 0;
}
