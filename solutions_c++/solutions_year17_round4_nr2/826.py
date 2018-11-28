#include <iostream>
#include <vector>
#include <utility>
#include <queue>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;

const int INF = 1e9;

int main () {
    cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);
    cout.setf(std::ios_base::fixed);
    cout.precision(24);
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int tt;
    cin >> tt;
    for (int t = 0; t < tt; ++t) {
        cout << "Case #" << t + 1 << ": ";
        int n, c, m;
        cin >> n >> c >> m;
        vector < multiset < int > > x(c);
        vector < int > dp(n);
        int bg = 0;
        for (int i = 0; i < m; ++i) {
            int a, p;
            cin >> p >> a;
            a--;
            p--;
            x[a].insert(p);
            dp[p]++;
            bg = max(bg, int(x[a].size()));
        }
        auto xc = x;
        int num = 0, deleted = 0;
        for (num = 1; ; ++num) {
            vector < int > used(c);
            for (int i = 0; i < n; ++i) {
                int findc = -1;
                int find = n + 10;
                for (int j = 0; j < c; ++j) {
                    if (used[j] || x[j].size() == 0) {
                        continue;
                    }
                    auto it = x[j].lower_bound(i);
                    if (it == x[j].end()) {
                        continue;
                    }
                    if (find > *it) {
                        find = *it;
                        findc = j;
                    }
                }
                if (findc == -1) {
                    break;
                }
                used[findc] = 1;
                x[findc].erase(x[findc].find(find));
                deleted++;
            }
            if (deleted == m) {
                break;
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, dp[i] - num);
        }
        cout << num  << " " << ans << "\n";
        //cout << res + add << "\n";
        cerr << "done " << t + 1 << endl;
    }
    return 0;
}


