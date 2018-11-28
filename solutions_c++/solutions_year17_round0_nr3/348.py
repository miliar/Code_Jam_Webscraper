#include <algorithm>
#include <cassert>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define setmin(a,b) a = min(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define MP make_pair
#define A first
#define B second
#define RF(i,a,b) for(int i=(a)-1;i>=(b);--i)
#define BEND(v) (v).begin(),(v).end()
#define SZ(v) int((v).size())
#define FORI(i,v) FOR(i,SZ(v))
typedef long double ld;
typedef long long ll;

ll N;
ll K;
void doit(int cas)
{
    scanf(" %lld %lld", &N, &K);
    --K;

    map<ll, ll> q;
    q[N] = 1;

    ll a, b;
    while (true) {
        ll len = q.rbegin()->first;
        ll cnt = q[len];

        b = (len-1) / 2;
        a = (len-1) - b;

        //printf("Split %lld into %lld %lld\n", len, a, b);

        if (cnt > K) break;

        K -= cnt;
        q.erase(len);

        q[a] += cnt;
        q[b] += cnt;
    }

    printf("Case #%d: %lld %lld\n", cas, a, b);
}

int T;
int main()
{
    scanf(" %d", &T);
    assert(1 <= T && T <= 100);
    FOR(cas,T) doit(cas+1);
    return 0;
}
