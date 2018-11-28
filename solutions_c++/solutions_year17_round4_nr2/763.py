#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 2017;

int tc, n, c, m;
int oa, ob, noa, nob;
vector<int> a, b;
bool used[MAX_N];

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> n >> c >> m;
        oa = ob = noa = nob = 0;
        a.resize(0);
        b.resize(0);
        fill(used, used + m, 0);
        for (int i = 0; i < m; i++) {
            int x, y;
            cin >> x >> y;
            if (y == 1) {
                if (x == 1) {
                    oa++;
                } else {
                    noa++;
                    a.push_back(x);
                }
            } else {
                if (x == 1) {
                    ob++;
                } else {
                    nob++;
                    b.push_back(x);
                }
            }
        }
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        int ans1 = oa + ob + max(max(0, noa - ob), max(0, nob - oa));
        int ans2 = min(max(0, noa - ob), max(0, nob - oa));
        for (int i = 0; i < a.size(); i++) {
            for (int j = 0; j < b.size(); j++) {
                if (!used[j] && b[j] != a[i]) {
                    ans2--;
                    used[j] = 1;
                    break;
                }
            }
        }
        cout << ans1 << " " << max(0, ans2) << "\n";
    }
}

