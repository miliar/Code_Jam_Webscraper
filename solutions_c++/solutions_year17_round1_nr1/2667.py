#include <algorithm>
#include <array>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <queue>
#include <sstream>
#include <limits>
#include <list>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <set>
#include <vector>
#include <regex>

using namespace std;

bool solve_brute(vector<string> &f, set<char> &chs, int i, int j) {
    for (char ch : chs) {
        f[i][j] = ch;
        bool had = false;
        for (int ii = i; ii < f.size(); ++ii) {
            for (int jj = 0; jj < f[0].length(); ++jj) {
                if (f[ii][jj] == '?') {
                    if (solve_brute(f, chs, ii, jj)) return true;
                    had = true;
                }
            }
        }

        if (!had) {
            unordered_map<char, pair<pair<int, int>, pair<int, int>>> rect;
            for (int ii = 0; ii < f.size(); ++ii) {
                for (int jj = 0; jj < f[0].length(); ++jj) {
                    if (rect.find(f[ii][jj]) == rect.end()) {
                        rect[f[ii][jj]] = make_pair(make_pair(ii, jj), make_pair(ii, jj));
                    }

                    rect[f[ii][jj]].first.first = min(rect[f[ii][jj]].first.first, ii);
                    rect[f[ii][jj]].first.second = min(rect[f[ii][jj]].first.second, jj);
                    rect[f[ii][jj]].second.first = max(rect[f[ii][jj]].second.first, ii);
                    rect[f[ii][jj]].second.second = max(rect[f[ii][jj]].second.second, jj);
                }
            }

            bool ok = true;
            for (auto i1 : rect) {
                if (!ok) break;
                for (auto i2 : rect) {
                    if (i1.first != i2.first && ok) {
                        int minx1 = i1.second.first.first;
                        int miny1 = i1.second.first.second;
                        int maxx1 = i1.second.second.first;
                        int maxy1 = i1.second.second.second;
                        int minx2 = i2.second.first.first;
                        int miny2 = i2.second.first.second;
                        int maxx2 = i2.second.second.first;
                        int maxy2 = i2.second.second.second;

                        if (minx2 <= maxx1 && minx1 <= maxx2 && miny2 <= maxy1 && miny1 <= maxy2)
                            ok = false;
                    }
                }
            }
            if (ok) return true;
        }
    }
    f[i][j] = '?';

    return false;

}

vector<string> solve(vector<string> &f) {
    set<char> chs;
    int r = f.size();
    int c = f[0].length();
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            if (f[i][j] != '?') {
                chs.insert(f[i][j]);
            }
        }
    }

    int ri = -1;
    int rj = -1;
    bool had = false;
    for (int i = 0; i < r && !had; ++i) {
        for (int j = 0; j < c && !had; ++j) {
            if (f[i][j] == '?') {
                solve_brute(f, chs, i, j);
                had = true;
            }
        }
    }

    return f;
}

int main() {
    cin.sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int r, c;
        cin >> r >> c;
        vector<string> f(r, "");
        for (int i = 0; i < r; ++i) {
            cin >> f[i];
        }
        vector<string> res = solve(f);
        cout << "Case #" << t << ": " << endl;
        for (int i = 0; i < r; ++i) {
            cout << res[i] << endl;
        }
    }

    return 0;
}
