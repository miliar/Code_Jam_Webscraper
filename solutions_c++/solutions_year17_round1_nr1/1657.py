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

int r,c;
string s[30];
int main()
{
    freopen("al.in","r",stdin);
    freopen("al.out","w",stdout);
    int t=0,T;
    cin>>T;
    while(++t<=T)
    {
        cin>>r>>c;
        REP(i,0,r-1)cin>>s[i];
        PII init=MP(-1,-1);
        REP(i,0,r-1)
        {
            REP(j,0,c-1)
            {
                if(s[i][j]!='?')
                {
                    init=MP(i,j);
                    break;
                }
            }
            if(init.first!=-1)break;
        }
        while(init.first!=0)
        {
            init.first--;
            REP(j,0,c-1)s[init.first][j]=s[init.first+1][j];
        }
//        while(init.second!=0)
//        {
//            init.second--;
//            s[init.first][init.second]=s[init.first][init.second+1];
//        }
        REP(i,0,r-1)
        {
            init=MP(-1,-1);
            REP(j,0,c-1)
            {
                if(s[i][j]!='?')
                {
                    init=MP(i,j);
                    break;
                }
            }
            if(init.first==-1)
            {
                REP(j,0,c-1)s[i][j]=s[i-1][j];
                continue;
            }
            REP(j,0,c-1)
            {
                if(s[i][j]!='?')
                {
                    init=MP(i,j);
                }
                else
                {
                    s[i][j]=s[init.first][init.second];
                }
            }
        }
        cout<<"Case #"<<t<<":\n";
        REP(i,0,r-1)cout<<s[i]<<"\n";
    }
    return 0;
}

