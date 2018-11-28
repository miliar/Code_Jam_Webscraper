#include <algorithm>
#include <cassert>
#include <cstring>
#include <deque>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>

int main() {
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/in.txt", "r", stdin);
    // std::freopen("C:/Users/Admin/Documents/Visual Studio 2015/Projects/hackerrank/Debug/out.txt", "w", stdout);

    int tn;
    std::cin >> tn;

    for (int ti = 1; ti <= tn; ++ti) {
        int r;
        int c;
        std::cin >> r >> c;

        std::vector<std::string> g(r + 1);
        for (int i = 1; i <= r; ++i) {
            std::string s;
            std::cin >> s;
            g[i] = '_' + s;
        }

        std::set<char> used;
        for (int i = 1; i <= r; ++i) {
            for (int j = 1; j <= c; ++j) {
                auto x = g[i][j];
                if (x == '?') {
                    continue;
                }
                if (used.count(x)) {
                    continue;
                }
                used.insert(x);
                int fj = j;
                int tj = j;
                while (fj - 1 >= 1) {
                    auto y = g[i][fj - 1];
                    if (y != x && y != '?') {
                        break;
                    }
                    --fj;
                }
                while (tj + 1 <= c) {
                    auto y = g[i][tj + 1];
                    if (y != x && y != '?') {
                        break;
                    }
                    ++tj;
                }
                int fi = i;
                int ti = i;
                while (fi - 1 >= 1) {
                    bool ok = true;
                    for (int k = fj; k <= tj; ++k) {
                        auto y = g[fi - 1][k];
                        if (y != x && y != '?') {
                            ok = false;
                            break;
                        }
                    }
                    if (!ok) {
                        break;
                    }
                    --fi;
                }
                while (ti + 1 <= r) {
                    bool ok = true;
                    for (int k = fj; k <= tj; ++k) {
                        auto y = g[ti + 1][k];
                        if (y != x && y != '?') {
                            ok = false;
                            break;
                        }
                    }
                    if (!ok) {
                        break;
                    }
                    ++ti;
                }
                for (int ii = fi; ii <= ti; ++ii) {
                    for (int jj = fj; jj <= tj; ++jj) {
                        g[ii][jj] = x;
                    }
                }
            }
        }

        std::cout << "Case #" << ti << ":\n";
        for (int i = 1; i <= r; ++i) {
            for (int j = 1; j <= c; ++j) {
                std::cout << g[i][j];
                assert(g[i][j] != '?');
            }
            std::cout << '\n';
        }
    }
}