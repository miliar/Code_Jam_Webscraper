#include <bits/stdc++.h>

using namespace std;

const int P = 7;

int p3[P];

void init() {
    p3[0] = 1;
    for (int i = 1; i < P; i++)
        p3[i] = p3[i - 1] * 3;
}

int bit(int mask, int pos) {
    mask /= p3[pos];
    return mask % 3;
}

struct Solver {

    vector<string> field;
    int max_mask;
    int n, m;
    vector<vector<char>> dp;
    vector<vector<int>> par_mask;
    vector<vector<string>> config;
    vector<string> ans;

    void rec(int col, int mask) {
        if (col == 0)
            return;
        rec(col - 1, par_mask[col][mask]);
        ans.push_back(config[col][mask]);
    }


    void solve() {
        cin >> n >> m;
        field.resize(n);
        for (int i = 0; i < n; i++)
            cin >> field[i];
        max_mask = p3[n];
        dp.assign(m + 1, vector<char>(max_mask));
        par_mask.assign(m + 1, vector<int>(max_mask));
        config.assign(m + 1, vector<string>(max_mask));
        dp[0][0] = true;
        for (int col = 0; col < m; col++) {
            for (int old_m = 0; old_m < max_mask; old_m++) {
                if (!dp[col][old_m])
                    continue;
                vector<int> beams;
                bool bad_mask = false;
                for (int r = 0; r < n; r++)
                    if (field[r][col] == '-' || field[r][col] == '|') {
                        if (bit(old_m, r) == 1)
                            bad_mask = true;
                        beams.push_back(r);
                    }
                if (bad_mask)
                    continue;
                int sz = beams.size();
                for (int bm = 0; bm < (1 << sz); bm++) {
                    string cur(n, '.');
                    for (int r = 0; r < n; r++)
                        cur[r] = field[r][col];
                    for (int i = 0; i < sz; i++)
                        if (bm & (1 << i))
                            cur[beams[i]] = '-';
                        else
                            cur[beams[i]] = '|';
                    vector<bool> was(n);
                    for (int i = 0; i < n; i++)
                        if (cur[i] == '|') {
                            int x = i - 1;
                            while (x >= 0) {
                                if (cur[x] == '#')
                                    break;
                                was[x] = true;
                                x--;
                            }
                            x = i + 1;
                            while (x < n) {
                                if (cur[x] == '#')
                                    break;
                                was[x] = true;
                                x++;
                            }
                        }
                    bool ok = true;
                    for (int i = 0; i < n; i++) {
                        if ((cur[i] == '|' || cur[i] == '-') && was[i])
                            ok = false;
                    }
                    for (int i = 0; i < n; i++)
                        if (cur[i] != '-' && cur[i] != '.' && bit(old_m, i) == 2)
                            ok = false;
                    for (int i = 0; i < n; i++) {
                        if (cur[i] == '-') {
                            int y = col - 1;
                            while (y >= 0 && field[i][y] != '#') {
                                if (field[i][y] == '|' || field[i][y] == '-')
                                    ok = false;
                                y--;
                            }
                            y = col + 1;
                            while (y < m && field[i][y] != '#') {
                                if (field[i][y] == '|' || field[i][y] == '-')
                                    ok = false;
                                y++;
                            }
                        }
                    }
                    if (!ok)
                        continue;
                    int new_mask = 0;
                    for (int i = 0; i < n; i++) {
                        if (cur[i] == '#') 
                            continue;
                        if (bit(old_m, i) == 1 || cur[i] == '-') {
                            new_mask += p3[i];
                            continue;
                        }
                        if (bit(old_m, i) == 2 || (cur[i] == '.' && !was[i] && bit(old_m, i) != 1))
                            new_mask += 2 * p3[i];
                    }
                    dp[col + 1][new_mask] = true;
                    par_mask[col + 1][new_mask] = old_m;
                    config[col + 1][new_mask] = cur;
                }
            }
        }
        int mask = -1;
        for (int ms = 0; ms < max_mask; ms++) {
            bool ok = true;
            for (int b = 0; b < n; b++)
                if (bit(ms, b) == 2)
                    ok = false;
            if (ok && dp[m][ms])
                mask = ms;
        }
        if (mask == -1) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        cout << "POSSIBLE" << endl;
        rec(m, mask);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                cout << ans[j][i];
            cout << endl;
        }
    }
};

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(20);
    init();
    int ts;
    cin >> ts;
    for (int t = 1; t <= ts; t++) {
        cout << "Case #" << t << ": ";
        Solver solver;
        solver.solve();
    }
}
