//#define _GLIBCXX_DEBUG
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <climits> 
#include <cfloat> 
#include <map> 
#include <utility> 
#include <set> 
#include <iostream> 
#include <memory> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <sstream> 
#include <complex> 
#include <stack> 
#include <queue> 
#include <numeric>
#include <cassert>
#include <gmpxx.h>

#define FOR(i, min, max) for (int i = (min); i < (max); ++i) 
#define FORE(i, min, max) for (int i = (min); i <= (max); ++i) 
#define REP(i, n) for (int i = 0; i < (n); ++i) 
#define REPV(vec, i) for (int i = 0; i < (int)(vec.size()); ++i) 
#define FOR_EACH(vec, it) for (typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); ++it)

using namespace std; 
static const double EPS = 1e-12; 
typedef long long ll; 
typedef mpz_class bint;

template<typename T>
string toS(const T &d) {
    ostringstream oss;
    oss << d;
    return oss.str();
}

set<pair<ll, ll> > mem;

void recur(ll n, ll k)
{
    assert(n >= k);
    if (k == 0)
        return;
    //cerr << n << "," << k << endl;
    pair<ll, ll> key(n, k);
    if (mem.find(key) != mem.end())
        return;
    mem.insert(key);
    recur(n/2, (k)/2);
    recur((n-1)/2, (k-1)/2);
}

string solve(ll N, ll K)
{
    mem.clear();
    //cerr << "-- recur -- " << endl;
    recur(N, K);
    ll n = N;
    //cerr << "-- solve -- " << endl;
    for (auto &p : mem) {
        if (p.second == 1) {
            n = min(n, p.first);
        }
    }
    return toS((n)/2LL) + " " + toS((n-1)/2LL);
}

string solveSimple(ll N, ll K)
{
    priority_queue<ll> Q;
    Q.push(N);
    for (ll i=0; i<K-1; i++) {
        ll n = Q.top();
        assert(n > 0);
        Q.pop();
        if (n % 2 == 0) {
            assert((n/2)+(n/2-1)+1 == n);
            Q.push(n/2);
            Q.push(n/2-1);
        }
        else {
            assert((n/2)+(n/2)+1 == n);
            Q.push(n/2);
            Q.push(n/2);
        }
    }
    ll n = Q.top();
    return toS((n)/2LL) + " " + toS((n-1)/2LL);
}

int main(void)
{
#if 0
    {
        int N = 4;
        for (int K=1; K<=N; K++) {
            cerr << N << "," << K << endl;
            string ans = solve(N, K);
            assert(solve(N, K) == solveSimple(N, K));
        }
    }
#endif
    int T;
    cin >> T;
    REP(_t, T) {
        ll K, N;
        cin >> N >> K;
        string ans = solve(N, K);
#if 0
        cerr << ans << endl;
        cerr << solveSimple(N, K) << endl;
        assert(solve(N, K) == solveSimple(N, K));
#endif
        cout << "Case #" << _t+1 << ": " << ans << endl;
    }

    return 0;
}
