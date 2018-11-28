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
const ll LINF = (ll)INF * INF;
const ld EPS = 1e-9;


ld solve(ld d, const vector<ld> &poses, const vector<ld> &speeds) {
    ld res = 1e30;
    
    for (int i = 0; i != poses.size(); ++i) {
        res = min(res, max(speeds[i] * d / (d - poses[i]), speeds[i]));
    }
    
    return res;
}


int main() {
    ios_base::sync_with_stdio(false);
    // cin.tie(0);
    
    cout.precision(20);
    cout << fixed;
    
    int tests;
    cin >> tests;
    
    for (int test = 0; test != tests; ++test) {
        int d, n;
        cin >> d >> n;
        
        vector<ld> poses(n), speeds(n);
        for (int i = 0; i != n; ++i) {
            cin >> poses[i] >> speeds[i];
        }
        
        cout << "Case #" << test + 1 << ": " << solve(d, poses, speeds) << "\n";
    }
    
    return 0;
}