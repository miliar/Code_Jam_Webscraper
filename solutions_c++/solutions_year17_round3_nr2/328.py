#include <iostream>

using namespace std;

int t, c, j;
pair<pair<int, int>, bool> a[200];
int z[1441][1441][2];

int f(int t, int r, bool g, int i = 0) {
    if (t == 1440) return !r ? 0 : 1e9;
    if (z[t][r][g] < 2e9) return z[t][r][g];
    while (i < c + j && a[i].first.second <= t) ++i;
    int m = 1e9;
    if (i < c + j && a[i].first.first == t) {
        bool w = a[i].second == g;
        m = min(m, f(a[i].first.second, a[i].second ? r : r - (a[i].first.second - a[i].first.first), !a[i].second, i) + w);
    }
    else {
        m = min(m, min(f(t + 1, g ? r - 1 : r, g, i), f(t + 1, g ? r : r - 1, !g, i) + 1));
    }
    return z[t][r][g] = m;
}

int main() {
    cin >> t;
    for (int _ = 0; _ ++< t;) {
        for (int i = 0; i < 1441; ++i) for (int j = 0; j < 1441; ++j) z[i][j][0] = z[i][j][1] = 2e9;
        cin >> c >> j;
        for (int i = 0; i < c + j; ++i) cin >> a[i].first.first >> a[i].first.second, a[i].second = i < c;
        sort(a, a + c + j);
        int y = min(f(0, 720, 0), f(0, 720, 1));
        y = (y + 1) / 2 * 2;
        cout << "Case #" << _ << ": " << y << '\n';
    }
}
