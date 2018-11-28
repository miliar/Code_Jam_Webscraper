#include <iostream>
#include <vector>
#include <utility>
#include <fstream>
#include <cassert>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

vector < vector < int > > ok = {
        {2, 3, 4},
        {4},
        {0, 4, 5},
        {0},
        {0, 1, 2},
        {2}
};

vector < char > to_color = {'R', 'O', 'Y', 'G', 'B', 'V'};

bool check (vector < int > x) {
    int n = x.size();
    x.push_back(x.front());
    for (int i = 1; i < n; ++i) {
        int find = 0;
        for (int j = 0; j < ok[x[i]].size(); ++j) {
            find += (x[i - 1] == ok[x[i]][j]);
            find += (x[i + 1] == ok[x[i]][j]);
        }
        if (find != 2) {
            return false;
        }
    }
    return true;
}

vector < int > solve_stupid (vector < int > x) {
    int n = 0;
    int mxidx = 0;
    for (int i = 0; i < 6; ++i) {
        n += x[i];
        if (x[i] > x[mxidx]) {
            mxidx = i;
        }
    }
    vector < int > ans(n);
    int last = -1;
    for (int i = 0; i < n; ++i) {
        if (last != mxidx && x[mxidx]) {
            ans[i] = mxidx;
            x[mxidx]--;
        } else {
            int mx = 0, idx = last;
            for (int j = 0; j < x.size(); ++j) {
                if (j == last) {
                    continue;
                }
                if (x[j] > mx) {
                    idx = j;
                    mx = x[j];
                }
            }
            x[idx]--;
            ans[i] = idx;
        }
        last = ans[i];
    }
    return ans;
}

vector < int > bad = {1, 3, 5};


int main () {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);
    cout.setf(std::ios_base::fixed);
    cout.precision(8);
    cerr.setf(std::ios_base::fixed);
    cerr.precision(25);
    int tt;
    cin >> tt;
    for (int t = 0; t < tt; ++t) {
        cout << "Case #" << t + 1 << ": ";
        int n;
        cin >> n;
        vector < int  > x(6);
        // cerr << t << endl;
        int sum = 0;
        for (int i = 0; i < 6; ++i) {
            cin >> x[i];
            sum += (x[i] != 0);
        }
        if (sum == 1) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        if (sum == 2) {
            vector < int > res(n);
            for (int i = 0; i < n; ) {
                for (int j = 0; j < 6; ++j) {
                    if (x[j] > 0) {
                        res[i] = j;
                        ++i;
                        x[j]--;
                    }
                }
            }
            if (!check(res)) {
                cout << "IMPOSSIBLE\n";
            } else {
                for (int i = 0; i < n; ++i) {
                    cout << to_color[res[i]];
                }
                cout << "\n";
            }
            continue;
        }
        bool could = true;
        for (auto p: bad) {
            if (x[p] == 0) {
                continue;
            }
            if (x[p] >= x[ok[p][0]]) {
                could = false;
            }
        }
        if (!could) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        vector < int > rpl(6);
        for (auto p: bad) {
            rpl[p] = x[p];
            x[ok[p][0]] -= x[p];
            x[p] = 0;
        }
        auto res = solve_stupid(x);
        if (!check(res)) {
            cout << "IMPOSSIBLE\n";
        } else {
            vector < int > ans;
            for (int i = 0; i < res.size(); ++i) {
                ans.push_back(res[i]);
                for (int j = 0; j < rpl.size(); ++j) {
                    if (rpl[j] == 0) {
                        continue;
                    }
                    if (res[i] == ok[j][0]) {
                        for (int k = 0; k < rpl[j]; ++k) {
                            ans.push_back(j);
                            ans.push_back(res[i]);
                        }
                        rpl[j] = 0;
                    }
                }
            }
            assert(ans.size() == n);
            for (int i = 0; i < n; ++i) {
                cout << to_color[ans[i]];
            }
            cout << "\n";
        }
    }
    return 0;
}


