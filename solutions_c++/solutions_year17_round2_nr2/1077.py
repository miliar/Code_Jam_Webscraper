#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ll;
typedef long double ld;
const double PI = acos(-1.);


int main() {
    freopen("/home/york_io/Documents/Code/contest/in.txt", "r", stdin);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string ans = "IMPOSSIBLE";
        int n, r, o, y, g, b, v;
        cin >> n >> r >> o >> y >> g >> b >> v;
        int fl = 1;
        string cur(n, ' ');
        // r, y, b
        vector<pair<int, char>> pn(3);
        pn[0] = make_pair(r, 'R');
        pn[1] = make_pair(y, 'Y');
        pn[2] = make_pair(b, 'B');
        sort(pn.begin(), pn.end());
        for (int i = 0; i < pn[2].first && fl; ++i) {
            if (2 * i >= n - 1) {
                fl = 0;
                continue;
            }
            cur[2 * i] = pn[2].second;
        }
        int left = pn[0].first;
        for (int i = 0; i < pn[0].first && fl; ++i) {
            int id = 2 * (pn[2].first + i);
            if (id < n) {
                cur[id] = pn[0].second;
                --left;
            }
        }
        int id = 1;
        while (left) {
            cur[id] = pn[0].second;
            --left;
            id += 2;
        }


        for (int i = 1; i < n; ++i) {
            if (cur[i] == ' ') {
                cur[i] = pn[1].second;
            }
            if (cur[i] == cur[i - 1]) {
                fl = 0;
            }
        }

        if (fl) ans = cur;

        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}
