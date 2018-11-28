#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
#include <cassert>
using namespace std;

#define SD(a) scanf("%d", &a)
#define SDD(a, b) scanf("%d%d", &a, &b)
#define SDDD(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define SDDDD(a, b, c, d) scanf("%d%d%d%d", &a, &b, &c, &d)
#define SL(a) scanf("%lld", &a)
#define SC(a) scanf("%c", &a)
#define PD(a) printf("%d", a)
#define PS(a) printf("%s", a)
#define PF(a) printf("%0.6lf", a)
#define PL(a) printf("%lld\n", a)
#define PN printf("\n")

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define SFOR(i,a,b,c) for(int i=a;i<b;i+=c)
#define REP(i,n) FOR(i,0,n)
#define RFOR(i,a,b) for(int i=a;i>=b;i--)
#define RREP(i,n) RFOR(i,n-1,0)
#define ECH(it, v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define ALL(x) (x).begin(),(x).end()
#define SRT(x) sort(ALL(x))
#define CLR(x) memset(x,0,sizeof(x))
#define SET(x) memset(x,-1,sizeof(x))
#define MOD 1000000007
typedef long long LL;
typedef unsigned int UI;
typedef unsigned long long UL;
typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;
typedef pair<int, int> PI;

void solve() {
    LL n, k;
    SL(n);
    SL(k);
    LL a[2][2]; //big, small
    CLR(a);
    a[0][0] = n, a[0][1] = 1;
    while(k>0) {
        a[0][0]--, a[1][0]--;
        if(a[0][0] < 0) a[0][0] = a[0][1] = 0;
        if(a[1][0] < 0) a[1][0] = a[1][1] = 0;
        LL e = a[0][0]/2;
        LL o = ((a[0][0]&1)? a[0][0]:a[1][0]) - e;
        if(o < 0) o = 0;
        LL ec = a[1][1] + a[0][1] + ((~a[0][0]&1)? a[0][1]:a[1][1]);
        LL oc = ((a[0][0]&1)? a[0][1]:a[1][1]);
        if(k <= a[0][1]) {
            cout<<max(a[0][0]-e, e)<<" "<<min(a[0][0]-e, e)<<endl;
            return;
        }
        if(k <= a[0][1] + a[1][1]) {
            cout<<max(a[1][0]-e, e)<<" "<<min(a[1][0]-e, e)<<endl;
            return;
        }
        k -= a[0][1] + a[1][1];
        if(o > e) {
            a[0][0] = o, a[0][1] = oc;
            a[1][0] = e, a[1][1] = ec;
        } else {
            a[0][0] = e, a[0][1] = ec;
            a[1][0] = o, a[1][1] = oc;
        }
    }
    assert(false);
}

int main() {
#ifdef raaja
    freopen("/home/raaja/Desktop/input.txt", "r", stdin);
    //freopen("/home/raaja/Desktop/output.txt", "w", stdout);
#endif
    int qq = 1, zz;
    SD(qq);
    zz = qq;
    while(qq--) {
        printf("Case #%d: ", zz-qq);
        solve();
    }
    return 0;
}
