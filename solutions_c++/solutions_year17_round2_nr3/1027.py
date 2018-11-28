#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>

#define f first
#define s second

using namespace std;

vector<int> e;
vector<int> s;
vector<vector<double>> memo;
vector<vector<int>> d;
int n, q;

double ans(int pos, int horse, int health) {
    if (health < 0) {
        return 1e12;
    }
    if (pos == n - 1) {
        return 0;
    }
    if (memo[pos][horse] > 0) {
        return memo[pos][horse];
    }
    double res = ans(pos + 1, horse, health - d[pos][pos + 1]) + d[pos][pos + 1] * 1. / s[horse];
    res = min(res, ans(pos + 1, pos, e[pos] - d[pos][pos + 1]) + d[pos][pos + 1] * 1. / s[pos]);
    return memo[pos][horse] = res;
}

int main() {
    int T;
    cin >> T;
    for (int u = 0; u < T; ++u) {
        cin >> n >> q;
        e.resize(n);
        s.resize(n);
        d.assign(n, vector<int>(n));
        memo.assign(n, vector<double>(n, -1));
        for (int i = 0; i < n; ++i) {
            cin >> e[i] >> s[i];
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> d[i][j];
            }
        }
        int x, y;
        cin >> x >> y;
        cout.precision(10);
        double res = ans(1, 0, e[0] - d[0][1]) + d[0][1] * 1. / s[0];
        cout << "Case #" << u + 1 << ": " << fixed << res << "\n";
    }
    return 0;
}
