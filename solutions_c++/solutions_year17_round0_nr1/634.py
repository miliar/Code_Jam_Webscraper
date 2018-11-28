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
char f[11111];
int k;
int main(int argc, char const *argv[])
{
    RI(t);
    REP(kase, t) {
        RS(f);
        RI(k);
        int n = strlen(f);
        int ans = 0;
        for(int i=0;i<=n-k;++i) {
            if(f[i] == '-') {
                ans++;
                for(int j=i;j<i+k;++j){
                    if(f[j] == '-')f[j] = '+';
                    else f[j] = '-';
                }
            }
        }
        bool fg = 1;
        for(int i=n-k+1;i<n;++i)if(f[i] == '-')fg = 0;
        if(fg) {
            printf("Case #%d: %d\n",kase+1, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", kase+1);
        }
    }
    return 0;
}