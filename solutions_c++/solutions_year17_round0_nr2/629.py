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
int d[20];
int main(int argc, char const *argv[])
{
    RI(t);
    REP(kase, t) {
        cin>>n;
        int idx=0;
        while(n) {
            d[idx++] = n%10;
            n/=10;
        }
        bool f = 1;
        int wh;
        for(int i=0;i<idx-1;++i)if(d[i] < d[i+1]){
            f = 0;
            wh = i;
        }

        if(!f) {
            for(int i=0;i<=wh;++i)d[i] = 9;
            d[wh+1]--;
            for(int i=wh+1;i<idx-1;++i) {
                if(d[i] < d[i+1]) {
                    d[i] = 9;
                    d[i+1]--;
                } else break;
            }
        }
        LL ans = 0;
        for(int i=idx-1;i>=0;--i)ans = ans*10+d[i];
        printf("Case #%d: %lld\n", kase+1, ans);
    }
    return 0;
}