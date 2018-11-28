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
    string s;
    cin>>s;
    int n = s.length();
    int a[n];
    REP(i, n) a[i] = s[i]-'0';
    REP(i, n-1) {
        if(a[i] > a[i+1]) {
            int j = i;
            a[j]--;
            while(j > 0 && a[j-1] > a[j]) a[j-1]--, j--;
            j++;
            while(j < n) a[j] = 9, j++;
            break;
        }
    }
    bool flag = false;
    REP(i, n) {
        if(flag) PD(a[i]);
        else if(a[i]) {
            PD(a[i]);
            flag = true;
        }
    }
    PN;
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
