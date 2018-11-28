#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, cas = 1;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector <pair <int, int>> v;
        for (int i = 0; i < n; ++i)
            v.push_back ({i, n - i - 1});
        int ls, rs;    
        for (int i = 0; i < k; ++i) {
            int p = 0;
            for (int j = 0; j < n; ++j) {
                if (v[j].first == v[j].second && v[j].first == INT_MAX)
                    continue;
                if (min (v[p].first, v[p].second) < min (v[j].first, v[j].second)
                || (v[p].first == INT_MAX && v[p].second == INT_MAX))
                    p = j;
                else if (min (v[p].first, v[p].second) == min (v[j].first, v[j].second)) {
                    if (max (v[p].first, v[p].second) < max (v[j].first, v[j].second))
                        p = j;
                }
            }
            ls = v[p].first, rs = v[p].second;
            v[p].first = v[p].second = INT_MAX;
            for (int j = p - 1; j >= 0; --j) {
                if (v[j].first == v[j].second && v[j].first == INT_MAX)
                    break;
                v[j].second = p - j - 1;
            }
            for (int j = p + 1; j < n; ++j) {
                if (v[j].first == v[j].second && v[j].first == INT_MAX)
                    break;
                v[j].first = j - p - 1;
            }
        }
        cout << "Case #" << cas << ": " << max (ls, rs) << ' ' << min (ls, rs) << '\n';
        cas += 1;
    }
    return 0;
}
