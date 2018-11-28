#include <stdio.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>
#include <queue>

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long int64;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const long long inf64 = ((long long)1 << 62) - 1;
const long double pi = acos(-1);

template <class T> T sqr (T x) {return x * x;}
template <class T> T abs (T x) {return x < 0 ? -x : x;}

int main () {
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tc;
    cin >> tc;
    for (int ti = 0; ti < tc; ++ti) {
        int n, m;
        cin >> n >> m;

        vector<vector<char>> init(n, vector<char>(n, '.'));
        for (int i = 0; i < m; ++i) {
            int x, y;
            char c;
            cin >> c >> x >> y;
            --x, --y;
            init[x][y] = c;
        }

        vector<vector<bool>> a(n, vector<bool>(n, false));
        vector<vector<bool>> b(n, vector<bool>(n, false));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                a[i][j] = init[i][j] == 'x' || init[i][j] == 'o';
                b[i][j] = init[i][j] == '+' || init[i][j] == 'o';
            }
        }

        vector<bool> used_x(n, false);
        vector<bool> used_y(n, false);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (a[i][j]) {
                    used_x[i] = true;
                    used_y[j] = true;
                }
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (!used_x[i] && !used_y[j]) {
                    a[i][j] = true;
                    used_x[i] = true;
                    used_y[j] = true;
                }
            }
        }

        vector<bool> used_sum(2 * n - 1, false);
        vector<bool> used_diff(2 * n - 1, false);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (b[i][j]) {
                    used_sum[i + j] = true;
                    used_diff[i - j + n - 1] = true;
                }
            }
        }

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j <= i; ++j) {
                int x = j;
                int y = i - j;
                if (!used_sum[x + y] && !used_diff[x - y + n - 1]) {
                    b[x][y] = true;
                    used_sum[x + y] = true;
                    used_diff[x - y + n - 1] = true;
                }
            }
            if (i == n - 1) {
                break;
            }
            for (int j = 0; j <= i; ++j) {
                int x = n - 1 - j;
                int y = n - 1 - i + j;
                if (!used_sum[x + y] && !used_diff[x - y + n - 1]) {
                    b[x][y] = true;
                    used_sum[x + y] = true;
                    used_diff[x - y + n - 1] = true;
                }
            }
        }

        vector<vector<char>> res(n, vector<char>(n, '.'));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (a[i][j]) {
                    res[i][j] = b[i][j] ? 'o' : 'x';
                } else {
                    res[i][j] = b[i][j] ? '+' : '.';
                }
            }
        }

        int res_score = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                res_score += res[i][j] == 'x' || res[i][j] == 'o';
                res_score += res[i][j] == '+' || res[i][j] == 'o';
            }
        }

        vector<pair<pair<int, int>, char>> new_cells;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (init[i][j] != res[i][j]) {
                    new_cells.pb(mp(mp(i, j), res[i][j]));
                }
            }
        }

        cout << "Case #" << ti + 1 << ": " << res_score << " " << sz(new_cells) << endl;
        for (int i = 0; i < sz(new_cells); ++i) {
            cout << new_cells[i].sc << " " << new_cells[i].fs.fs + 1 << " " << new_cells[i].fs.sc + 1 << endl;
        }
    }

    return 0;
}