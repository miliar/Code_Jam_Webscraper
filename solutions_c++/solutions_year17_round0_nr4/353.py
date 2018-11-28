
#include <algorithm>
#include <iostream>
#include <cassert>
#include <set>
#include <sstream>
#include <vector>

using namespace std;

constexpr static int MAXN = 200;

int n, m;
int g[MAXN][MAXN];

constexpr static int NO_EDGE = -(1 << 30);

bool find_match(int i, const vector <vector <int>>& w,
        vector <int>& mr, vector <int>& mc, vector <int>& seen) {
    if (seen[i])
        return false;
    seen[i] = true;
    for (int j = 0; j < w[i].size(); j++) {
        if (w[i][j] != NO_EDGE && mc[j] < 0) {
            mr[i] = j;
            mc[j] = i;
            return true;
        }
    }
    for (int j = 0; j < w[i].size(); j++) {
        if (w[i][j] != NO_EDGE && mr[i] != j) {
            if (mc[j] < 0 || find_match(mc[j], w, mr, mc, seen)) {
                mr[i] = j;
                mc[j] = i;
                return true;
            }
        }
    }
    return false;
}

int match(const vector<vector <int>>& w, vector <int>& mr, vector <int>& mc) {
    mr = vector <int>(w.size(), -1);
    mc = vector <int>(w[0].size(), -1);
    vector <int> seen(w.size());

    int cnt = 0;
    for (int i = 0; i < w.size(); i++) {
        fill(seen.begin(), seen.end(), 0);
        if (find_match(i, w, mr, mc, seen))
            cnt++;
    }
    return cnt;
}

string solve() {
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            g[i][j] = 0;
    for (int k = 0; k < m; k++) {
        string s;
        int i, j;
        cin >> s >> i >> j;
        i--, j--;
        if (s[0] == '+')
            g[i][j] = 1;
        else if (s[0] == 'x')
            g[i][j] = 2;
        else
            g[i][j] = 3;
    }

    int R = n + (2 * n - 1), C = n + (2 * n - 1);
    vector <vector <int>> w(R);
    for (int i = 0; i < R; i++)
        w[i] = vector <int>(C, NO_EDGE);

    int score = 0;
    vector <int> row_used(n), col_used(n), d1_used(2 * n - 1), d2_used(2 * n - 1);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (g[i][j] & 1)
                score++, d1_used[i + j] = true, d2_used[i - j + n - 1] = true;
            if (g[i][j] & 2)
                score++, row_used[i] = true, col_used[j] = true;
        }

    ostringstream oss;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (g[i][j] == 0 || g[i][j] == 1) {
                if (!row_used[i] && !col_used[j])
                    w[i][j] = 1;
            }
            if (g[i][j] == 0 || g[i][j] == 2) {
                if (!d1_used[i + j] && !d2_used[i - j + n - 1])
                    w[n + i + j][n + i - j + n - 1] = 1;
            }
        }
    // cout << score << endl;

    vector <int> mr, mc;
    score += match(w, mr, mc);

    set <pair <int, int>> added;
    for (int i = 0; i < n; i++)
        if (mr[i] != -1) {
            int j = mr[i];
            added.insert({i, j});
            g[i][j] |= 2;
        }
    for (int sum = 0; sum < R - n; sum++)
        if (mr[n + sum] != -1) {
            int diff = mr[n + sum] - n - (n - 1);
            int i = (sum + diff) / 2; // (i + j) + (i - j) = 2*i
            int j = sum - i;
            added.insert({i, j});
            g[i][j] |= 1;
        }

    oss << score << ' ' << added.size() << '\n';
    const static char vals[] = {'+', 'x', 'o'};
    for (auto& p : added) {
        oss << vals[g[p.first][p.second] - 1] << ' '
            << p.first + 1 << ' ' << p.second + 1 << '\n';
    }
    return oss.str();
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " << solve();
    }
}
