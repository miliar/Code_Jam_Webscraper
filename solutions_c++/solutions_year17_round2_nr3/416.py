#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/detail/standard_policies.hpp>

using namespace std;
using namespace __gnu_pbds;
using namespace __gnu_cxx;

#define inf (1<<30)-1
#define INF (1LL<<62)-1
#define MOD 1000000007LL
#define MP make_pair
#define PB push_back
#define ALL(x) x.begin(),x.end()
#define PI acos(-1)
#define MEM(x,y) memset(x,y,sizeof (x))
#define debug cout<<"A"<<'\n'
#define REP(i,a,b) for (int i=(a); i<=(b); i++)
#define PER(i,a,b) for (int i=(a); i>=(b); i--)
#define REPL(i,a,b) for (LL i=(a); i<=(b); i++)
#define PERL(i,a,b) for (LL i=(a); i>=(b); i--)
#define print(x) cout<<x<<'\n'
#define itrALL(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define UNIQUE(X) X.erase( unique( X.begin(), X.end() ), X.end() )


typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int>PII;
typedef pair<LL,LL>PLL;
typedef vector<int> VI;
typedef vector<LL> VL;


// Order Statistic Tree

/* Special functions:

        find_by_order(k) --> returns iterator to the kth largest element counting from 0
        order_of_key(val) --> returns the number of items in a set that are strictly smaller than our item
*/

typedef tree<
PII,
null_type,
less<PII>,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;

template <class T> inline T bigmod(T p,T e,T M)
{
    T ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}

template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}
template <class T, class X> inline bool getbit(T a, X i) { T t=1; return ((a&(t<<i))>0);}
template <class T, class X> inline T setbit(T a, X i) { T t=1;return (a|(t<<i)); }
template <class T, class X> inline T resetbit(T a, X i) { T t=1;return (a&(~(t<<i)));}

/*end of header*/

LL n,q,d[103][103];
PLL horse[103];
double tmm[103][103];
int main()
{
    freopen("cll.in","r",stdin);
    freopen("cll.out","w",stdout);
    int t=0,T,u,v;
    scanf("%d",&T);
    while(++t<=T)
    {
        scanf("%lld %lld",&n,&q);
        REP(i,1,n)scanf("%lld %lld",&horse[i].first,&horse[i].second);//distance, speed
        REP(i,1,n)
        {
            REP(j,1,n)
            {
                scanf("%lld",&d[i][j]);
                if(d[i][j]==-1)d[i][j]=INF;
            }
        }

        for(int k=1;k<=n;k++)
            for(int i=1;i<=n;i++)
                for(int j=1;j<=n;j++)
                    d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
        REP(i,1,n)
        {
            REP(j,1,n)
            {
                if(d[i][j]>horse[i].first)tmm[i][j]=1e18;
                else
                {
                    double HS=horse[i].second,D=d[i][j];
                    tmm[i][j]=D/HS;
                }
            }
        }

        for(int k=1;k<=n;k++)
            for(int i=1;i<=n;i++)
                for(int j=1;j<=n;j++)
                    tmm[i][j]=min(tmm[i][j],tmm[i][k]+tmm[k][j]);

        printf("Case #%d:",t);
        REP(i,1,q)
        {
            scanf("%d %d",&u,&v);
            printf(" %.8f",tmm[u][v]);
        }
        printf("\n");

    }
    return 0;
}

