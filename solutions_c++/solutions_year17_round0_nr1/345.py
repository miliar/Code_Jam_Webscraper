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

int len;
char buf[1024];
bool init[1024];
bool flipped[1024];
int K;
void doit(int cas)
{
    scanf(" %s %d", buf, &K);
    len = strlen(buf);

    FOR(i,len) init[i] = buf[i] == '-';

    int ans = 0;
    bool failed = false;

    bool roll = false;
    FOR(i,len) {
        int j = i-K;
        if (j >= 0 && flipped[j]) roll = !roll;

        flipped[i] = roll != init[i];
        if (flipped[i]) {
            ++ans;
            roll = !roll;
        }

        if (i+K > len && flipped[i]) failed = true;
    }


    printf("Case #%d: ", cas);
    if (failed) {
        printf("IMPOSSIBLE\n");
    } else {
        printf("%d\n", ans);
    }
}

int T;
int main()
{
    scanf(" %d", &T);
    assert(1 <= T && T <= 100);
    FOR(cas,T) doit(cas+1);
    return 0;
}
