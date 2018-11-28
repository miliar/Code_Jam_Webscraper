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
const ll LINF = (ll)INF * INF;
const ld EPS = 1e-9;


ld solve(int n, int k, vector<pair<ll, ll>> &p) {
    sort(p.begin(), p.end());
    
    multiset<ll> max_heights;
    ll heights_sum = 0;
    ll answer = 0;
    
    for (auto const &pancake : p) {
        ll height = 2 * pancake.first * pancake.second;
        answer = max(answer, height + heights_sum + pancake.first * pancake.first);
        
        if (max_heights.size() < k - 1 || *max_heights.begin() < height) {
            assert(max_heights.size() <= k - 1);
            if (max_heights.size() == k - 1) {
                heights_sum -= *max_heights.begin();
                max_heights.erase(max_heights.begin());
            }
            heights_sum += height;
            max_heights.insert(height);
        }
    }
    
    return M_PI * (ld)answer;
}


int main() {
    ios_base::sync_with_stdio(false);
    
    cout.precision(20);
    cout << fixed;
    
    int tests;
    cin >> tests;
    
    for (int test = 0; test != tests; ++test) {
        int n, k;
        cin >> n >> k;
        
        vector<pair<ll, ll>> p(n);
        for (auto &elem : p) cin >> elem.first >> elem.second;
        cout << "Case #" << test + 1 << ": " << solve(n, k, p) << "\n";
    }
    
    return 0;
}