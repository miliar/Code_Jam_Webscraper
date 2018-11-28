#define _USE_MATH_DEFINES

#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int INF = 1000 * 1000 * 1000 + 11;


pair<int, int> solve(int n, int c, const vector<pair<int, int>> &boughts) {
    vector<int> cnt(c, 0), place(n, 0);
    for (const auto &p : boughts) {
        place[p.first - 1]++;
        cnt[p.second - 1]++;
    }
    
    int need = *max_element(cnt.begin(), cnt.end());
    int sum_prefix = 0;
    
    for (int i = 0; i != n; ++i) {
        sum_prefix += place[i];
        need = max(need, (sum_prefix + i) / (i + 1));
    }
    
    int res = 0;
    for (int val : place) {
        res += max(0, val - need);
    }
    
    return {need, res};
}


int main() {
    ios_base::sync_with_stdio(false);
    
    int tests;
    cin >> tests;
    
    for (int test = 0; test != tests; ++test) {
        cout << "Case #" << test + 1 << ": ";
        
        int n, c, m;
        cin >> n >> c >> m;
        vector<pair<int, int>> b(m);
        for (auto &p : b) cin >> p.first >> p.second;
        
        auto res = solve(n, c, b);
        cout << res.first << ' ' << res.second;
        
        cout << "\n";
    }
    
    return 0;
}