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

int N,K;
vector<pair<int,int>> stock; // (height, radius)
double calc_side(double r, double h)
{
    return 2 * M_PI * r * h;
}
double calc_top(double r)
{
    return M_PI * r * r;
}
bool stock_lt(pair<int,int> const & a, pair<int,int> const & b)
{
    return calc_side(a.second, a.first) < calc_side(b.second, b.first);
}
void doit(int cas)
{
    scanf(" %d %d", &N, &K);

    stock.clear();

    FOR(i,N) {
        int r,h;
        scanf(" %d %d", &r, &h);
        stock.push_back(MP(h,r));
    }
    sort(BEND(stock), stock_lt);
    reverse(BEND(stock));

    int topr = 0;
    FOR(i,K) topr = max(topr, stock[i].second);

    double prefix = 0;
    FOR(i,K-1) {
        prefix += calc_side(stock[i].second, stock[i].first);
    }
    double best = prefix + calc_side(stock[K-1].second, stock[K-1].first) + calc_top(topr);

    FR(i,K,N) if (stock[i].second > topr) {
        double now = prefix + calc_side(stock[i].second, stock[i].first) + calc_top(stock[i].second);
        if (now > best) best = now;
    }

    printf("Case #%d: %.9f\n", cas, best);
}

int T;
int main()
{
    scanf(" %d", &T);
    assert(1 <= T && T <= 100);
    FOR(cas,T) doit(cas+1);
    return 0;
}
