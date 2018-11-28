#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int ct = 1; ct <= t; ct++) {
        int r, c;
        string s;
        cin >> r >> c;
        vector<string> grid;
        for (int i = 0; i < r; i++) {
            cin >> s;
            grid.push_back(s);
        }

        int lastr = -1;
        string pstr = "";
        for (int i = 0; i < r; i++) {
            int f = 0;
            bool found = false;
            char pre = '?';
            for (int j = 0; j < c; j++) {
                if (grid[i][j] != '?') {
                    found = true;
                    fill(grid[i].begin()+f, grid[i].begin()+j, grid[i][j]);
                    pre = grid[i][j];
                    f = j+1;
                }
            }
            if (f < c) fill(grid[i].begin()+f, grid[i].end(), pre);
            if (found) pstr = grid[i];


            if (!found && lastr == -1) lastr = i;

            if (found && lastr != -1) {
                for (int k = lastr; k < i; k++)
                    grid[k] = grid[i];
                lastr = -1;
            }
        }
        if (lastr != -1) {
            for (int k = lastr; k < r; k++)
                grid[k] = pstr;
        }

        cout << "Case #" << ct <<  ":" << endl;
        for (string s : grid) cout << s << endl;
    }
}