#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ld = long double;

#define __fail() cout << "IMPOSSIBLE\n"; continue;

int n, k;

class Pie {
public:
    Pie(int r, int h, int idx) : r(r), h(h), idx(idx) { }

    ll r, h, idx;
};

vector<Pie> p;
vector<Pie> real_p;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int TT;
    cin >> TT;
    for (int T = 0; T < TT; ++T) {
        cout << "Case #" << T + 1 << ": ";
        cin >> n >> k;
        p.clear();
        p.reserve(n);
        int r, h;
        for (int i = 0; i < n; ++i) {
            cin >> r >> h;
            p.emplace_back(r, h, i);
        }
        real_p = p;
        ll best_res = 0;
        for (Pie& b : real_p) {  // bottom
            sort(p.begin(), p.end(), [&b](const Pie& lhs, const Pie& rhs) {
                if (lhs.r > b.r && rhs.r <= b.r) {
                    return true;
                }
                if (rhs.r > b.r && lhs.r <= b.r) {
                    return false;
                }
                if (lhs.r > b.r) {  // both >
                    return false;  // equal
                }
                return lhs.h * lhs.r > rhs.h * rhs.r;
            });
            ll current_res = b.r * b.r + 2 * b.r * b.h;
            int cur_c = 1;
            for (Pie& pie : p) {
                if (pie.r <= b.r && cur_c < k && pie.idx != b.idx) {
                    ++cur_c;
                    current_res += 2 * pie.r * pie.h;
                    if (cur_c == k) {
                        break;
                    }
                }
            }
            if (cur_c == k && current_res > best_res) {
                best_res = current_res;
            }
        }
        cout << fixed << setprecision(10) << M_PI * best_res << "\n";
    }

    return 0;
}