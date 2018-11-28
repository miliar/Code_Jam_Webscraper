#include<bits/stdc++.h>
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
#define MASK(i) (1LL<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define div   ___div
#define next   ___next
#define prev   ___prev
#define left   ___left
#define right   ___right
#define __builtin_popcount __builtin_popcountll
using namespace std;
template<class X,class Y>
    void minimize(X &x,const Y &y) {
        if (x>y) x=y;
    }
template<class X,class Y>
    void maximize(X &x,const Y &y) {
        if (x<y) x=y;
    }
template<class T>
    T Abs(const T &x) {
        return (x<0?-x:x);
    }

/* Author: Van Hanh Pham */

/** END OF TEMPLATE - ACTUAL SOLUTION COMES HERE **/

struct Triple {
    int x, y, z;

    Triple(int _x = -1, int _y = -1, int _z = -1) {
        x = _x; y = _y; z = _z;
    }

    bool operator < (const Triple &t) const {
        if (x != t.x) return x < t.x;
        if (y != t.y) return y < t.y;
        return z > t.z;
    }
};

pair<int, int> brute(int n, int m) {
    set<int> s;
    s.insert(0); s.insert(n + 1);

    Triple best;
    REP(love, m) {
        best = Triple(-1, -1, -1);
        FOR(i, 1, n) if (s.find(i) == s.end()) {
            __typeof(s.begin()) it = s.upper_bound(i);
            int R = *it - i - 1; it--;
            int L = i - *it - 1;
            maximize(best, Triple(min(L, R), max(L, R), i));
        }
        s.insert(best.z);
    }

    return make_pair(best.y, best.x);
}

pair<long long, long long> calcRes(long long x) {
    long long pos = (x + 1) >> 1;
    long long L = pos - 1;
    long long R = x - pos;
    return make_pair(max(L, R), min(L, R));
}

pair<long long, long long> solve(long long n, long long k) {
    map<long long, long long> cnt;
    priority_queue<long long> q;
    cnt[n] = 1;
    q.push(n);

    while (!q.empty()) {
        long long x = q.top(); q.pop();
        long long num = cnt[x];
        if (num >= k) return calcRes(x);
        k -= num;

        long long pos = (x + 1) >> 1;
        long long L = pos - 1;
        long long R = x - pos;
        if (cnt.find(L) == cnt.end()) q.push(L); cnt[L] += num;
        if (cnt.find(R) == cnt.end()) q.push(R); cnt[R] += num;
    }

    assert(false);
}

int main(void) {
    int t; cin >> t;
    REP(love, t) {
        if ((love + 1) % 5 == 0) cerr << love + 1 << endl;
        long long n, k; cin >> n >> k;
        pair<long long, long long> res = solve(n, k);
        printf("Case #%d: %lld %lld\n", love + 1, res.fi, res.se);
    }
    return 0;
}

/*** LOOK AT MY CODE. MY CODE IS AMAZING :D ***/
