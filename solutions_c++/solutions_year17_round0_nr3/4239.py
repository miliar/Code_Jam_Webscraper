//
//  main.cpp
//  test
//
//  Created by Lodour on 17/3/18.
//  Copyright © 2017年 Lodour. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <iomanip>
#include <functional>
#include <cstdlib>
#include <climits>
#include <cctype>
#include <sstream>
using namespace std;
#define REP(i,x) for(int i = 0; i < (x); i++)
#define DEP(i,x) for(int i = (x) - 1; i >= 0; i--)
#define FOR(i,x) for(__typeof(x.begin())i=x.begin(); i!=x.end(); i++)
#define CLR(a,x) memset(a, x, sizeof(a))
#define MO(a,b) (((a)%(b)+(b))%(b))
#define ALL(x) (x).begin(), (x).end()
#define SZ(v) ((int)v.size())
#define UNIQUE(v) sort(ALL(v)); v.erase(unique(ALL(v)), v.end())
#define out(x) cout << #x << ": " << x << endl;
#define fastcin ios_base::sync_with_stdio(0);cin.tie(0);
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;
typedef vector<int> VI;
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define EPS 1e-8
#define MP(x,y) make_pair(x,y)
#define MT(x,y...) make_tuple(x,y) // c++0x only
#define PB(x) push_back(x)
#define IT iterator
#define X first
#define Y second

class Range {
public:
    ll l, r;
    Range(ll _l, ll _r) {
        l = _l;
        r = _r;
    }
    // via length of range (reverse)
    bool operator < (const Range & y) const {
        if (r - l != y.r - y.l)
            return r - l < y.r - y.l;
        return l < y.l;
    }
    // get mid
    ll getmid() {
        return floor(0.5 * (l + r));
    }
    
    bool empty() {
        return l + 1 >= r;
    }
};

void solve(ll n, ll k, ll& rmax, ll& rmin) {
    priority_queue<Range, vector<Range>, less<Range>> pq;
    pq.push(Range(1, n));
    Range rg(0,0);
    while (k--) {
        rg = pq.top();
        pq.pop();
        ll mid = rg.getmid();
//        cout << rg.l << " " << rg.r << " " << mid << endl;
//        cout << "PUT " << rg.l << " " << mid - 1 << endl;
//        cout << "PUT " << mid + 1 << " " << rg.r << endl;
        if (mid - 1 >= rg.l) pq.push(Range(rg.l, mid - 1));
        if (mid + 1 <= rg.r) pq.push(Range(mid + 1, rg.r));
    }
    ll mid = rg.getmid();
//    cout << rg.l << " " << rg.r << endl;
    rmax = rg.r - mid;
    rmin = mid - rg.l;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/Lodour/Downloads/C-small-2-attempt0.in", "r", stdin);
    freopen("/Users/Lodour/Downloads/C-small-2-attempt0.out", "w", stdout);
    int t, cnt = 0;
    cin >> t;
    while (t--) {
        ll n, k;
        cin >> n >> k;
        ll rmax, rmin;
        solve(n, k, rmax, rmin);
        printf("Case #%d: %lld %lld\n", ++cnt, rmax, rmin);
    }
    return 0;
}
