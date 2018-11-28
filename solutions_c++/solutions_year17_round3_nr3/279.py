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

// valid for small dataset 1 only
const double EPS = 1e-8;

int N,K;
double U;
double P[64];
void readrat(double * p)
{
    scanf(" %lf", p);
}
void doit(int cas)
{
    scanf(" %d %d", &N, &K);

    readrat(&U);
    FOR(i,N) readrat(&P[i]);

    while (true) {
        double minp = 1.0;
        FOR(i,N) minp = min(minp, P[i]);

        if (minp > 1.0-EPS) break;

        bool yes[64];
        FOR(i,N) yes[i] = P[i] < minp+EPS;

        double next = 1.0;
        FOR(i,N) if (!yes[i]) next = min(next, P[i]);

        int nyes = 0;
        FOR(i,N) if (yes[i]) ++nyes;

        double inc = next - minp;
        if (nyes*inc > U) {
            inc = U/nyes;
            U = 0.0;
        }

        FOR(i,N) if (yes[i]) P[i] += inc;

        U -= nyes*inc;

        if (U < EPS) break;
    }

    double ans = 1.0;
    FOR(i,N) ans *= P[i];

    printf("Case #%d: %.6f\n", cas, ans);
}

int T;
int main()
{
    scanf(" %d", &T);
    assert(1 <= T && T <= 100);
    FOR(cas,T) doit(cas+1);
    return 0;
}
