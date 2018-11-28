#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <utility>

using namespace std;

void print(vector<string>& grid)
{
    for (int i = 0; i < grid.size(); i++) {
        cout << grid[i] << "\n";
    }
}

bool isGood(vector<string>& grid)
{
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == '?') {
                return false;
            }
        }
    }
    return true;
}

bool isValid(int r, int c, vector<string>& grid, char myChar)
{
    return r >= 0 && r < grid.size() &&
           c >= 0 && c < grid[0].size() &&
           (grid[r][c] == '?' || grid[r][c] == myChar);
}

bool sweep(int lr, int lc, int rr, int rc, vector<string>& grid, char c)
{
    for (int i = lr; i <= rr; i++) {
        for (int j = lc; j <= rc; j++) {
            if (!isValid(i, j, grid, c)) {
                return false;
            }
        }
    }
    for (int i = lr; i <= rr; i++) {
        for (int j = lc; j <= rc; j++) {
            grid[i][j] = c;
        }
    }
}

void expand(int r, int c, vector<string>& grid)
{
    char myChar = grid[r][c];
    int dR, dC, r1, c1, r2, c2;
    r1 = r;
    dR = -1;
    while (sweep(r1 + dR, c, r1 + dR, c, grid, myChar)) {
        r1 += dR;
    }
    dC = -1;
    c1 = c;
    while (sweep(r1, c1 + dC, r, c1 + dC, grid, myChar)) {
        c1 += dC;
    }
    dR = 1;
    r2 = r;
    while (sweep(r2 + dR, c1, r2 + dR, c, grid, myChar)) {
        r2 += dR;
    }
    dC = 1;
    c2 = c;
    while (sweep(r1, c2 + dC, r2, c2 + dC, grid, myChar)) {
        c2 += dC;
    }
}

bool chain(map<char, vector<pair<int, int>>>& m, vector<char>& o, vector<string>& grid) {
    if (o.empty()) {
        bool good = isGood(grid);
        if (good) {
            print(grid);
        }
        return good;
    }
    char c = o.back();
    o.pop_back();
    auto& v = m[c];
    vector<string> newGrid;
    for (int i = 0; i < v.size(); i++) {
        newGrid = grid;
        expand(v[i].first, v[i].second, newGrid);
        if (chain(m, o, newGrid)) {
            return true;
        }
    }
    o.push_back(c);
    return false;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ":" << "\n";
        int R, C;
        cin >> R >> C;
        vector<string> grid;
        for (int i = 0; i < R; i++) {
            string s;
            cin >> s;
            grid.push_back(s);
        }

        set<char> uo;
        map<char, vector<pair<int, int>>> m;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (grid[i][j] != '?') {
                    m[grid[i][j]].push_back(make_pair(i,j));
                    uo.insert(grid[i][j]);
                }
            }
        }

        vector<char> o(uo.begin(), uo.end());
        chain(m, o, grid);
    }
}
