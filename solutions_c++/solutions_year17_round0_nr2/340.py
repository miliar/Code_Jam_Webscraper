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

char ds[256];
int D;
bool dp[256]; // true = may choose equal digit
char out[256];
void doit(int cas)
{
    scanf(" %s", ds);
    D = strlen(ds);
    assert(D >= 1);

    dp[D-1] = true;
    RF(i, D-1, 0) {
        if (ds[i] > ds[i+1]) {
            dp[i] = false;
        } else if (ds[i] < ds[i+1]) {
            dp[i] = true;
        } else {
            dp[i] = dp[i+1];
        }
    }

    bool equ = true;
    FOR(i,D) {
        if (equ) {
            if (dp[i]) {
                out[i] = ds[i];
            } else {
                assert(ds[i] != '0');
                out[i] = ds[i] - 1;
                equ = false;
            }
        } else {
            out[i] = '9';
        }
    }
    out[D] = '\0';

    char * ans = out;
    while (*ans == '0') ++ans;

    printf("Case #%d: %s\n", cas, ans);
}

int T;
int main()
{
    scanf(" %d", &T);
    assert(1 <= T && T <= 100);
    FOR(cas,T) doit(cas+1);
    return 0;
}
