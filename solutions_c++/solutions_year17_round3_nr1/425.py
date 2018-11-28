#define _CRT_SECURE_NO_WARNINGS
#pragma region template
#include <climits>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <bitset>
#include <map>
#include <queue>
#include <ctime>
#include <stack>
#include <set>
#include <list>
#include <random>
#include <deque>
#include <functional>
#include <fstream>
#include <complex>
#include <numeric>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <sstream>

using namespace std;

struct _{
    _(){
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.precision(30);
    }
} __;

#pragma endregion

typedef long double ld;
typedef long long ll;

void solve() {
    int n, k;
    cin >> n >> k;
    vector<pair<ld, ld>> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].first >> a[i].second;
    }
    sort(a.begin(), a.end());
    ld result = 0;
    ld pi = acos(-1.0);
    multiset<ld> ss;
    ld sum = 0;

    auto add = [&](ld a) {
        if (k == 1) return;
        if (ss.size() < k - 1) {
            sum += a;
            ss.insert(a);
        }
        else {
            if (*ss.begin() < a) {
                sum -= *ss.begin();
                ss.erase(ss.begin());
                
                sum += a;
                ss.insert(a);
            }
        }
    };

    for (int i = 0; i < n; i++) {
        if (i > 0) {
            add(a[i - 1].second * a[i - 1].first);
        }
        result = max(result, a[i].first * a[i].first + 2 * a[i].first * a[i].second + 2 * sum);
    }
    cout.precision(40);
    cout << pi * result;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
