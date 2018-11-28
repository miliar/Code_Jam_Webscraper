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
char g[33][33];
int n,m;
char c[33];
int idx [33];
int main(int argc, char const *argv[])
{
    RI(t);
    REP(kase, t) {
        RII(n,m);
        ZERO(c);
        ZERO(idx);
        REP(i,n)RS(g[i]);
        REP(i,n)REP(j,m)if(g[i][j] != '?') {
            char x = g[i][j];
            int k = j + 1;
            for(;k < m && g[i][k] == '?'; ++k)g[i][k] = x;
            k = j - 1;
            for(;k >= 0 && g[i][k] == '?'; --k)g[i][k] = x;
        }


        REP(i,n)if(g[i][0] == '?') {
            int k = i;
            bool f = 0;
            for(;k<n;k++) {
                if(g[k][0]!='?') {
                    f = 1;
                    break;
                }
            }
            if(!f) {
                k = i;
               for(;k>=0;k--) {
                    if(g[k][0]!='?') {
                        f = 1;
                        break;
                    }
                } 
            }
            for(int ii=0;ii<m;++ii)g[i][ii] = g[k][ii];
        }
        printf("Case #%d:\n", kase+1);
        REP(i,n)puts(g[i]);
    }
    return 0;
}