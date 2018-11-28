#include <bits/stdc++.h>

using namespace std;

map<int, vector<int>> he;

void cnt(int tl, int tr) {
    if (tl > tr)
        return;
    int len = tr - tl + 1;
    int tm = (tl + tr) / 2;
    he[len].push_back(tm);
    if (tl == tr)
        return;
    cnt(tl, tm - 1);
    cnt(tm + 1, tr);
}



void solve() {
    he.clear();
    int n, k;
    cin >> n >> k;
    cnt(0, n - 1);
    int c = 0;
    int last = 0;
    vector<char> used(n);
    for (auto it = he.rbegin(); it != he.rend(); ++it) {
        for (auto it2 : it->second) {
            last = it2;
            used[it2] = true;
            if (++c == k)
                break;
        }
        if (c == k)
            break;
    }
    int ls = 0, rs = 0;
    while (last - ls - 1 >= 0 && !used[last - ls - 1])
        ++ls;
    while (last + rs + 1 < n && !used[last + rs + 1])
        ++rs;
    cout << max(ls, rs) << " " << min(ls, rs) << endl;
}


int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t = 1;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cout << "Case #" << tt << ": ";
        solve();
    }

    return 0;
}
