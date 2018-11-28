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

int main() {
    int t;
    cin >> t;

    for (int no = 0; no < t; no++) {
        string s;
        int k;
        cin >> s >> k;

        int n = s.size();
        vector<int> state(n);

        for (int i = 0; i < n; i++) state[i] = (s[i] == '+') ? 1 : 0;

        int ans = 0;
        for (int i = 0; i + k - 1 < n; i++) {
            if (state[i] == 0) {
                ans++;
                for (int j = 0; j < k; j++) {
                    state[i + j] = (state[i + j] + 1) % 2;
                }
            }
        }

        bool valid = true;
        for (int i = 0; i < n; i++) {
            if (state[i] == 0) {
                valid = false;
                break;
            }
        }

        cout << "Case #" << no + 1 << ": ";
        if (valid) cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
