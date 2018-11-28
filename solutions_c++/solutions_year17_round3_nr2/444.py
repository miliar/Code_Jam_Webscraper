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


struct Segment {
    int begin, end;
    bool first;
    
    Segment(int begin, int end, bool first) : begin(begin), end(end), first(first) {}
    
    bool operator<(const Segment &seg) const {
        return begin < seg.begin;
    }
    
    static int dist(const Segment &a, const Segment &b, bool way = false) {
        if (b < a) return dist(b, a, way);
        
        if (!way) return b.begin - a.end;
        return a.begin - b.end + 24 * 60;
    }
};


int solve(const vector<pair<int, int>> &A, const vector<pair<int, int>> &B) {
    vector<Segment> segs;
    segs.reserve(A.size() + B.size());
    int sum_a = 0, sum_b = 0;
    
    for (const auto &seg : A) {
        segs.emplace_back(seg.first, seg.second, true);
        sum_a += seg.second - seg.first;
    }
    for (const auto &seg : B) {
        segs.emplace_back(seg.first, seg.second, false);
        sum_b += seg.second - seg.first;
    }
    
    vector<int> a, b;
    
    sort(segs.begin(), segs.end());
    segs.push_back(segs.front());
    int result = 0;
    
    for (auto it = segs.begin() + 1; it != segs.end(); ++it) {
        if (it->first == (it - 1)->first) {
            (it->first ? a : b).push_back(Segment::dist(*it, *(it - 1), it + 1 == segs.end()));
        } else {
            result += 1;
        }
    }
    
    sort(a.rbegin(), a.rend());
    sort(b.rbegin(), b.rend());
    
    while (!a.empty() && a.back() <= 24 * 60 / 2 - sum_a) {
        sum_a += a.back();
        a.pop_back();
    }
    
    while (!b.empty() && b.back() <= 24 * 60 / 2 - sum_b) {
        sum_b += b.back();
        b.pop_back();
    }
    
    result += a.size() * 2 + b.size() * 2;
    return result;
}


int main() {
    ios_base::sync_with_stdio(false);
    
    cout.precision(20);
    cout << fixed;
    
    int tests;
    cin >> tests;
    
    for (int test = 0; test != tests; ++test) {
        int a_size, b_size;
        cin >> a_size >> b_size;
        
        vector<pair<int, int>> a(a_size);
        for (auto &elem : a) cin >> elem.first >> elem.second;
        vector<pair<int, int>> b(b_size);
        for (auto &elem : b) cin >> elem.first >> elem.second;
        
        cout << "Case #" << test + 1 << ": " << solve(a, b) << "\n";
    }
    
    return 0;
}