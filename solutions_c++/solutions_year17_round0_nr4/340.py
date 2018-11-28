#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <memory.h>
#include <random>
#include <sstream>
#include <stdio.h>
#include <vector>
using namespace std;

int n, m;
char bd[101][101];
char bd_org[101][101];
char bd_best[101][101];
bool rows[101], cols[101];
bool dia1[201], dia2[201];

void solve()
{
    cin >> n >> m;
    vector<string> org(n, string(n, '.'));
    vector<vector<bool> > bd(n, vector<bool>(n, false));
    vector<vector<bool> > cd(n, vector<bool>(n, false));

    for (int i = 0; i < m; i++) {
        char v;
        int r, c;
        cin >> v >> r >> c;
        r--, c--;

        org[r][c] = v;

        if (v == 'o' || v == '+') {
            bd[r][c] = true;
        }
        if (v == 'o' || v == 'x') {
            cd[r][c] = true;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 2; j++) {
            int s = j ? i : n * 2 - 2 - i;

            int pos = -1, cnt = 0;
            for (int r = 0; r < n; r++) {
                int c = s - r;
                if (!(c >= 0 && c < n))
                    continue;

                if (bd[r][c] == false) {
                    bool ok = true;
                    for (int k = -n; k <= n; k++) {
                        int nr = r + k;
                        int nc = c + k;
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n && bd[nr][nc]) {
                            ok = false;
                            break;
                        }
                    }
                    if (ok)
                        pos = r;
                } else {
                    cnt++;
                }
            }

            if (cnt == 0 && pos >= 0) {
                bd[pos][s - pos] = true;
            }
        }
    }

    for (int r = 0; r < n; r++) {
        int pos = -1, cnt = 0;
        for (int c = 0; c < n; c++) {
            if (cd[r][c] == false) {
                bool ok = true;
                for (int rr = 0; rr < n; rr++) {
                    if (cd[rr][c]) {
                        ok = false;
                        break;
                    }
                }
                if (ok)
                    pos = c;
            } else {
                cnt++;
            }
        }
        if (cnt == 0 && pos >= 0) {
            cd[r][pos] = true;
        }
    }

    int score = 0;
    vector<string> ans(n, string(n, '.'));
    vector<pair<int, int> > changes;
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) {
            ans[r][c] = ".x+o"[(bd[r][c] ? 2 : 0) + (cd[r][c] ? 1 : 0)];
            score += bd[r][c] ? 1 : 0;
            score += cd[r][c] ? 1 : 0;
            if (org[r][c] != ans[r][c])
                changes.emplace_back(r, c);
        }
    }

    fprintf(stderr, "\n");
    for (auto& row : ans) {
        fprintf(stderr, "* %s\n", row.c_str());
    }

    printf("%d %d\n", score, (int)changes.size());
    for (auto& p : changes) {
        int r = p.first;
        int c = p.second;
        printf("%c %d %d\n", ans[r][c], r + 1, c + 1);
    }
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
