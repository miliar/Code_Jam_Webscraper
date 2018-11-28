#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
        size_t casenum;
        cin >> casenum;
        for (size_t caseid {1}; caseid <= casenum; ++caseid) {
                int R, C;
                cin >> R >> C;
                vector<string> grid(R);
                for (int i {0}; i < R; ++i)
                        cin >> grid[i];
                for (int i {0}; i < R; ++i) {
                        for (int j {0}; j < C; ++j) {
                                if (grid[i][j] == '?') continue;
                                int x {i - 1};
                                while (x >= 0 && grid[x][j] == '?') {
                                        grid[x][j] = grid[i][j];
                                        --x;
                                }
                        }
                }
                for (int i {0}; i < R; ++i) {
                        for (int j {0}; j < C; ++j) {
                                if (grid[i][j] == '?') continue;
                                int x {i + 1};
                                while (x < R && grid[x][j] == '?') {
                                        grid[x][j] = grid[i][j];
                                        ++x;
                                }
                        }
                }
                for (int i {0}; i < R; ++i) {
                        for (int j {0}; j < C; ++j) {
                                if (grid[i][j] == '?') continue;
                                int y {j - 1};
                                while (y >= 0 && grid[i][y] == '?') {
                                        grid[i][y] = grid[i][j];
                                        --y;
                                }
                        }
                }
                for (int i {0}; i < R; ++i) {
                        for (int j {0}; j < C; ++j) {
                                if (grid[i][j] == '?') continue;
                                int y {j + 1};
                                while (y < C && grid[i][y] == '?') {
                                        grid[i][y] = grid[i][j];
                                        ++y;
                                }
                        }
                }
                cout << "Case #" << caseid << ":\n";
                for (const auto& s : grid)
                        cout << s << '\n';
        }
        return 0;
}