// This code performs maximum bipartite matching.
//
// Running time: O(|E| |V|) -- often much faster in practice
//
//   INPUT: w[i][j] = edge between row node i and column node j
//   OUTPUT: mr[i] = assignment for row node i, -1 if unassigned
//           mc[j] = assignment for column node j, -1 if unassigned
//           function returns number of matches made

#include <cassert>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
    for (int j = 0; j < w[i].size(); j++) {
        if (w[i][j] && !seen[j]) {
            seen[j] = true;
            if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
                mr[i] = j;
                mc[j] = i;
                return true;
            }
        }
    }
    return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
    mr = VI(w.size(), -1);
    mc = VI(w[0].size(), -1);

    int ct = 0;
    for (int i = 0; i < w.size(); i++) {
        VI seen(w[0].size());
        if (FindMatch(i, w, mr, mc, seen)) ct++;
    }
    return ct;
}

VVI w;
VI lf, rg;
vector< pair<char, pair<int, int> > > operations;

set<int> row, col, diag1, diag2;
int n, m;

int main(void) {

    int test_num;
    cin >> test_num;

    for (int Case = 1 ; Case <= test_num ; ++Case) {

        cin >> n >> m;

        row.clear();
        col.clear();
        diag1.clear();
        diag2.clear();

        VVI inp(n+1, VI(n+1, 0));
        VVI ans(n+1, VI(n+1, 0));

        for (int i = 1 ; i <= n ; ++i) {
            row.insert(i);
            col.insert(i);
        }
        for (int i = 0 ; i < 2*n ; ++i) {
            diag1.insert(i);
            diag2.insert(i);
        }

        int current_score = 0;
        for (int i = 0 ; i < m ; ++i) {
            char ch;
            int r, c;
            cin >> ch >> r >> c;
            if (ch == 'x' or ch == 'o') {
                row.erase(r);
                col.erase(c);
                ans[r][c] = inp[r][c] = (ch == 'x' ? 1 : 3);
                ++current_score;
            }
            if (ch == '+' or ch == 'o') {
                diag1.erase(r+c-1);
                diag2.erase(r-c+n-1);
                ans[r][c] = inp[r][c] = (ch == '+' ? 2 : 3);
                ++current_score;
            }
        }

        assert(row.size() == col.size());
        for (auto it1 = row.begin(), it2 = col.begin() ; it1 != row.end() && it2 != col.end() ; it1++, it2++) {
            ans[*it1][*it2] += 1;
            ++current_score;
        }

        w.assign(2*n, VI(2*n, 0));
        lf.assign(2*n, -1);
        rg.assign(2*n, -1);

        for (int i = 1 ; i <= n ; ++i) {
            for (int j = 1 ; j <= n ; ++j) {
                int d1 = i + j - 1, d2 = i - j + n - 1;
                if (diag1.count(d1) and diag2.count(d2)) {
                    w[d1][d2] = 1;
                }
            }
        }

        const int total = current_score + BipartiteMatching(w, lf, rg);

        for (int d1 = 0 ; d1 < 2*n ; ++d1) {
            if (lf[d1] == -1) continue;
            int d2 = lf[d1];
            int r = (d1 + d2 - n + 2) / 2;
            int c = (d1 - d2 + n) / 2;
            ans[r][c] += 2;
        }

        operations.clear();
        for (int i = 1 ; i <= n ; ++i) {
            for (int j = 1 ; j <= n ; ++j) {
                if (ans[i][j] > inp[i][j]) {
                    operations.push_back({" x+o"[ans[i][j]], {i, j}});
                }
            }
        }

        cout << "Case #" << Case << ": " << total << " " << operations.size() << endl;
        for (auto ops : operations) {
            cout << ops.first << " " << ops.second.first << " " << ops.second.second << endl;
        }

        cerr << Case << endl;
    }

    return 0;
}
