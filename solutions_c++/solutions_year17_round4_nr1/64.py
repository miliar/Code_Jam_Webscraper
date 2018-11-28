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


vector<vector<vector<int>>> ways = {
    { {2} },
    { {1, 1}, {3, 0}, {0, 3} },
    { {1, 0, 1}, {0, 2, 0}, {2, 1, 0}, {0, 1, 2}, {4, 0, 0}, {0, 0, 4} }
};

int solve_stupid(int P, const vector<int> &v) {
    auto vv = v;
    sort(vv.begin(), vv.end());
    int best = 0;
    
    do {
        int sum = 0, res = 0;
        for (int i = 0; i != vv.size(); ++i) {
            if (sum == 0) ++res;
            sum = (sum + vv[i]) % P;
        }
        best = max(best, res);
    } while (next_permutation(vv.begin(), vv.end()));
    return best;
}

int solve(int P, const vector<int> &v) {
    int res = 0;
    vector<int> cnt(3);
    for (int val : v) {
        if (val % P == 0) {
            ++res;
        } else {
            cnt[val % P - 1]++;
        }
    }
    
    while (true) {
        for (auto const &way : ways[P - 2]) {
            bool ok = true;
            for (int i = 0; i != way.size(); ++i) {
                if (cnt[i] < way[i]) {
                    ok = false;
                    break;
                }
            }
            if (!ok) continue;
            
            for (int i = 0; i != way.size(); ++i) {
                cnt[i] -= way[i];
            }
            ++res;
            goto next;
        }
        
        break;
        next: {}
    }
    
    for (int val : cnt) {
        if (val) {
            ++res;
            break;
        }
    }
    
    return res;
}

void stress() {
    int P = rand() % 3 + 2;
    int N = rand() % 8 + 1;
    
    vector<int> g(N);
    for (int i = 0; i != N; ++i) {
        g[i] = rand() % 100 + 1;
    }
    
    int a = solve(P, g);
    int b = solve_stupid(P, g);
    
    assert(a == b);
}


int main() {
    ios_base::sync_with_stdio(false);
    
    int tests;
    cin >> tests;
    
    for (int test = 0; test != tests; ++test) {
        cout << "Case #" << test + 1 << ": ";
        
        int n, p;
        cin >> n >> p;
        
        vector<int> g(n);
        for (int &val : g) cin >> val;
        
        cout << solve(p, g) << '\n';
    }
    
    return 0;
}