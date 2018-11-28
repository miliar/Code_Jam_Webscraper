#define NDEBUG
NDEBUG


#include <algorithm>
#include <cassert>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <memory>
#include <random>

#define FOR(i, n) for (int i = 0; i < (n); ++i)


using namespace std;

// TC_REMOVE_BEGIN
/// caide keep
bool __hack = std::ios::sync_with_stdio(false);
/// caide keep
auto __hack1 = cin.tie(nullptr);
// TC_REMOVE_END


namespace template_util {
    

    constexpr int bytecount(uint64_t x) {
        return x ? 1 + bytecount(x >> 8) : 0;
    }

    /// caide keep
    template<int N>
    struct bytetype {
        
    };

    /// caide keep
    template<>
    struct bytetype<4> {
        
    };

    /// caide keep
    template<>
    struct bytetype<3> {
        
    };

    /// caide keep
    template<>
    struct bytetype<2> {
        
    };

    /// caide keep
    template<>
    struct bytetype<1> {
        
    };

    /// caide keep
    template<>
    struct bytetype<0> {
        
    };

    /// caide keep
    template<uint64_t N>
    struct minimal_uint : bytetype<bytecount(N)> {
    };
}


template<class T>
T next(istream& in) {
    T ret;
    in >> ret;
    return ret;
}


/*

++
x.

+x..+
..x.+
+..x+
.x..+
++x+.

x+
.x

x+++
.x..
..x.
.++x

x...t
+txt+
t.tx+
+o.t+
t.t.o
3 * (n-1) + 1
....
x.+.
....
...x

1 x, +, o
.....o..

+x.
+.o
x..


x++
.x.
.+x
*/

bool cross_on_diag[2][301];
bool x_on_col[101];
bool x_on_row[101];
int f[101][101];
int init_f[101][101];
int n;
int best_score = 0;
vector<vector<int>> actions;
//
//void rec(int row, int col) {
//    if (row >= n) {
//        if (best_score < cur_score) {
//            best_score = cur_score;
//            best_actions = actions;
//        }
//        return;
//    }
//    if (col >= n) {
//        rec(row + 1, 0);
//        return;
//    }
//
//    rec(row, col + 1);
//    if (f[row][col]) {
////        if (f[row][col] == 1 || f[row][col] == 2) {
////            if (f[row][col] == 1) {
////                // try o
////                if (!x_on_col[col] && !x_on_row[row]) {
////                    x_on_col[col] = true;
////                    x_on_row[row] = true;
////                    ++cur_score;
////                    actions.push_back({row, col, 3});
////                    rec(row, col + 1);
////                    actions.pop_back();
////                    x_on_col[col] = false;
////                    x_on_row[row] = false;
////                    --cur_score;
////                }
////            } else {
////                // try o
////                if (!cross_on_diag[0][n - 1 - row + col] && !cross_on_diag[1][row + col]) {
////                    cross_on_diag[0][n - 1 - row + col] = true;
////                    cross_on_diag[1][row + col] = true;
////                    ++cur_score;
////                    actions.push_back({row, col, 3});
////                    rec(row, col + 1);
////                    actions.pop_back();
////                    cross_on_diag[0][n - 1 - row + col] = false;
////                    cross_on_diag[1][row + col] = false;
////                    --cur_score;
////                }
////            }
////
////        }
//        return;
//    }
//
//    // try +
//    if (!cross_on_diag[0][n - 1 - row + col] && !cross_on_diag[1][row + col]) {
//        cross_on_diag[0][n - 1 - row + col] = true;
//        cross_on_diag[1][row + col] = true;
//        ++cur_score;
//        actions.push_back({row, col, 1});
//        rec(row, col + 1);
//        actions.pop_back();
//        cross_on_diag[0][n - 1 - row + col] = false;
//        cross_on_diag[1][row + col] = false;
//        --cur_score;
//    }
//    // try x
//    if (!x_on_col[col] && !x_on_row[row]) {
//        x_on_col[col] = true;
//        x_on_row[row] = true;
//        ++cur_score;
//        actions.push_back({row, col, 2});
//        rec(row, col + 1);
//        actions.pop_back();
//        x_on_col[col] = false;
//        x_on_row[row] = false;
//        --cur_score;
//    }
//    // try o
//    if (!x_on_col[col] && !x_on_row[row] && !cross_on_diag[0][n - 1 - row + col] && !cross_on_diag[1][row + col]) {
//        x_on_col[col] = true;
//        x_on_row[row] = true;
//        cross_on_diag[0][n - 1 - row + col] = true;
//        cross_on_diag[1][row + col] = true;
//        ++cur_score;
//        ++cur_score;
//        actions.push_back({row, col, 3});
//        rec(row, col + 1);
//        actions.pop_back();
//        x_on_col[col] = false;
//        x_on_row[row] = false;
//        cross_on_diag[0][n - 1 - row + col] = false;
//        cross_on_diag[1][row + col] = false;
//        --cur_score;
//        --cur_score;
//    }
//}

vector<vector<int>> data;

void solveTest(istream& in, ostream& out) {
    FOR(i, n) {
        FOR(j, n) {
            f[i][j] = 0;
        }
    }
    memset(x_on_col, false, sizeof x_on_col);
    memset(x_on_row, false, sizeof x_on_row);
    memset(cross_on_diag, false, sizeof cross_on_diag);

    best_score = 0;
    actions.clear();

    for (const auto& v : data) {
        int r = v[0];
        int c = v[1];
        int t = v[2];
        f[r][c] = t;
        if (t == 1) {
            cross_on_diag[0][n - 1 - r + c] = true;
            cross_on_diag[1][r + c] = true;
        } else if (t == 2) {
            x_on_col[c] = true;
            x_on_row[r] = true;
        } else {
            x_on_col[c] = true;
            x_on_row[r] = true;
            cross_on_diag[0][n - 1 - r + c] = true;
            cross_on_diag[1][r + c] = true;
        }
    }

    //rec(0, 0);
    FOR(i, n) {
        FOR(j, n) {
            init_f[i][j] = f[i][j];
        }
    }
    FOR(i, n) {
        FOR(j, n) {
            if (f[i][j] != 0) continue;
            if (!x_on_col[j] && !x_on_row[i]) {
                x_on_col[j] = true;
                x_on_row[i] = true;
                f[i][j] = 2;
            }
        }
    }
    FOR(i, n) {
        FOR(j, n) {
            if (f[i][j] != 0) continue;
            if (i == 0 || i == n-1 || j == 0 || j == n-1) {
                if (!cross_on_diag[0][n - 1 - i + j] && !cross_on_diag[1][i + j]) {
                    cross_on_diag[0][n - 1 - i + j] = true;
                    cross_on_diag[1][i + j] = true;
                    f[i][j] = 1;
                }
            }
        }
    }
    /*
    .x.
    +++
    x..
     */
    FOR(i, n) {
        FOR(j, n) {
            if (f[i][j] == 1) {
                if (!x_on_col[j] && !x_on_row[i]) {
                    f[i][j] = 3;
                    x_on_col[j] = true;
                    x_on_row[i] = true;
                }
            }
            if (f[i][j] == 2) {
                if (!cross_on_diag[0][n - 1 - i + j] && !cross_on_diag[1][i + j]) {
                    cross_on_diag[0][n - 1 - i + j] = true;
                    cross_on_diag[1][i + j] = true;
                    f[i][j] = 3;
                }
            }
        }
    }
    FOR(i, n) {
        FOR(j, n) {
            if (f[i][j] == 1) {
                best_score++;
            }
            if (f[i][j] == 2) {
                best_score++;
            }
            if (f[i][j] == 3) {
                best_score++;
                best_score++;
            }
            if (init_f[i][j] != f[i][j]) {
                actions.push_back({f[i][j], i, j});
            }
        }
    }
    out << best_score << ' ' << actions.size() << endl;
    for (const auto& v : actions) {
        if (v[0] == 1) {
            out << "+ " << v[1] + 1 << ' ' << v[2] + 1 << endl;
        } else if (v[0] == 2) {
            out << "x " << v[1] + 1 << ' ' << v[2] + 1 << endl;
        } else {
            out << "o " << v[1] + 1 << ' ' << v[2] + 1 << endl;
        }
    }
}

void inputData(istream& in) {
    n = next<int>(in);
    int m = next<int>(in);
    data.clear();
    while (m--) {
        string s = next<string>(in);
        int r = next<int>(in) - 1;
        int c = next<int>(in) - 1;
        int t = 3;
        if (s[0] == '+') {
            t = 1;
        }
        if (s[0] == 'x') {
            t = 2;
        }
        data.push_back({r, c, t});
    }
}

void solve(istream& in, ostream& out, const int test_id = -1) {
    int test = next<int>(in);
    FOR(t, test) {
        inputData(in);
        if (t == test_id || test_id == -1) {
            out << "Case #" << t + 1 << ": ";
            solveTest(in, out);
        }
    }
}
#include <fstream>


int main(int argc, char* argv[]) {
    if (argc == 0) {
        solve(cin, cout);
    } else {
        ifstream in("in.txt");
        int test_id = stoi(argv[1]);
        solve(in, cout, test_id);
    }
    return 0;
}

