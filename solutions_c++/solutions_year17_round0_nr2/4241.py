#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <stack>
#include <queue>
#include <functional>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <vector>
#include <array>
#include <tuple>
#include <utility>
#include <numeric>
#include <iomanip>
#include <cctype>
#include <cmath>
#include <assert.h>
#include <cstdlib>
#include <list>
using namespace std;

using ll = long long;
using ull = unsigned long long;
using PII = pair<int, int>;
using PLL = pair<ll, ll>;

template<typename T1, typename T2> ostream& operator<<(ostream& s, const pair<T1, T2>& p) {
    return s << "(" << p.first << ", " << p.second << ")";
}
template<typename T> ostream& operator<<(ostream& s, const vector<T>& v) {
    s << "[";
    for (int i = 0; i < v.size(); i++) s << (i == 0 ? "" : ", ") << v[i];
    s << "]";
    return s;
}

#define ALL(a) (a).begin(), (a).end()

ll dp[20][10][2];

int main() {
    int t;
    cin >> t;

    for (int no = 0; no < t; no++) {
        string str_n;
        cin >> str_n;

        cin.ignore();

        vector<int> vec_n(str_n.size());

        for (int i = 0; i < str_n.size(); i++) {
            vec_n[i] = str_n[i] - '0';
        }

        memset(dp, -1, sizeof(dp));
        dp[0][0][0] = 0;

        for (int i = 0; i < vec_n.size(); i++) {
            for (int last_d = 0; last_d <= 9; last_d++) {
                for (int less = 0; less <= 1; less++) {
                    for (int d = 0; d <= 9; d++) {
                        if ((!less && d > vec_n[i]) || last_d > d) continue;
                        dp[i + 1][d][less || (d < vec_n[i])]
                            = max(dp[i + 1][d][less || (d < vec_n[i])],
                                  dp[i][last_d][less] * 10 + (ll)d);
                    }
                }
            }
        }

        ll ans = 0;
        for (int last_d = 0; last_d <= 9; last_d++) {
            for (int less = 0; less <= 1; less++) {
                ans = max(ans, dp[vec_n.size()][last_d][less]);
            }
        }
        cout << "Case #" << no + 1 << ": " << ans << endl;
    }

    return 0;
}
