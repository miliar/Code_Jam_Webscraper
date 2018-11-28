#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <climits>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#define REP(i,n) for(int (i)=0;i<(int)(n);++(i))
#define REPIT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define PB push_back
#define FT first
#define SD second
#define ZERO(x) memset(x,0,sizeof(x))
#define NEG(x) memset(x,-1,sizeof(x))
#define RI(x) scanf("%d",&(x))
#define RII(x,y) scanf("%d%d",&(x),&(y))
#define RIII(x,y,z) scanf("%d%d%d",&(x),&(y),&(z))
#define OIII(x,y,z) printf("%d %d %d\n",(x),(y),(z))
#define OII(x,y) printf("%d %d\n",(x),(y))
#define OI(x) printf("%d\n",(x))
#define OL(x) cout<<(x)<<endl
#define OLL(x,y) cout<<(x)<<" "<<(y)<<endl
#define OLLL(x,y,z) cout<<(x)<<" "<<(y)<<" "<<(z)<<endl
#define RS(s) scanf("%s",(s))
#define MP(x,y) make_pair((x),(y))
#define SZ(x) ((int)(x).size())
#define FIN(f) freopen(f,"r",stdin)
#define FOUT(f) freopen(f,"w",stdout)
typedef long long LL;
using namespace std;
typedef pair<int,int> PII;
const int MOD = 1e9+7;
const int maxn = 222222;
int t;
LL n;
LL k;
int main(int argc, char const *argv[])
{
    RI(t);
    REP(kase, t) {
        cin>>n>>k;
        LL cum = 1;
        LL lev = 2;
        LL L = 1,R = 0;
        while(cum < k) {
            cum += lev;
            lev *= 2;
            LL nl,nr;
            if(n%2 == 0) {
                n = n / 2;
                nl = L;
                nr = L + R*2LL;
            } else {
                n = n/2;
                nl = L*2LL + R;
                nr = R;
            }
            L = nl;R = nr;
        }
        LL x;
        LL res = cum - k;
        if(res >= R) x = n;
        else x = n-1;

        LL l,r;
        if(x%2 == 0) {
            l = x/2;
            r = x/2-1;
        } else {
            l = r = x/2;
        }
        printf("Case #%d: %lld %lld\n",kase+1, l , r);
    }
    return 0;
}