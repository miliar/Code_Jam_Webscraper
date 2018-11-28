#include <bits/stdc++.h>

using namespace std;

const string I = "IMPOSSIBLE";
using pii = pair<int, int>;

struct Solver {
    void run() {
        int n;
        int r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        if (r * 2 > n || y * 2 > n || b * 2 > n) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        string s = "RYB";
        string ans(n, '0');
        vector<pii> a{{r, 0}, {y, 1}, {b, 2}};
        sort(a.rbegin(), a.rend());
        vector<int> pos;
        for (int i = 0; i < n; i++)
            if (i % 2 == 0)
                pos.push_back(i);
        for (int i = 0; i < n; i++)
            if (i % 2 == 1)
                pos.push_back(i);
        int cur = 0;
        for (int i = 0; i < n; i++) {
            if (a[cur].first == 0)
                cur++;
            a[cur].first--;
            ans[pos[i]] = s[a[cur].second];
        }
        cout << ans << endl;
    }
};

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(20);

    int ts;
    cin >> ts;
    for (int t = 1; t <= ts; t++) {
        cout << "Case #" << t << ": ";
        Solver solver;
        solver.run();
    }
}
