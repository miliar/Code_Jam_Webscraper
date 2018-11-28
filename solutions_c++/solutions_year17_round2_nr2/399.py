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

// only r,y,b
int main()
{
    freopen("bss.in","r",stdin);
    freopen("bss.out","w",stdout);
    int t=0,T,n,r,o,y,g,b,v;
    scanf("%d",&T);
    while(++t<=T)
    {
        scanf("%d %d %d %d %d %d %d",&n,&r,&o,&y,&g,&b,&v);
        if(r>y+b || y>r+b || b>r+y)
        {
            printf("Case #%d: IMPOSSIBLE\n",t);
            continue;
        }
        printf("Case #%d: ",t);
        if(r>=y && r>=b)
        {
            int lst=0;
            while(r>0)
            {
                printf("R");
                r--;
                if(y>b)
                {
                    lst=1;
                    printf("Y");
                    y--;
                }
                else
                {
                    lst=0;
                    printf("B");
                    b--;
                }
            }
            while(y+b>0)
            {
                if(lst==1)
                {
                    printf("B");
                    b--;
                    lst=0;
                }
                else
                {
                    printf("Y");
                    y--;
                    lst=1;
                }
            }
        }

        if(y>=r && y>=b)
        {
            int lst=0;
            while(y>0)
            {
                printf("Y");
                y--;
                if(r>b)
                {
                    lst=1;
                    printf("R");
                    r--;
                }
                else
                {
                    lst=0;
                    printf("B");
                    b--;
                }
            }
            while(r+b>0)
            {
                if(lst==1)
                {
                    printf("B");
                    b--;
                    lst=0;
                }
                else
                {
                    printf("R");
                    r--;
                    lst=1;
                }
            }
        }

        if(b>=r && b>=y)
        {
            int lst=0;
            while(b>0)
            {
                printf("B");
                b--;
                if(y>r)
                {
                    lst=1;
                    printf("Y");
                    y--;
                }
                else
                {
                    lst=0;
                    printf("R");
                    r--;
                }
            }
            while(y+r>0)
            {
                if(lst==1)
                {
                    printf("R");
                    r--;
                    lst=0;
                }
                else
                {
                    printf("Y");
                    y--;
                    lst=1;
                }
            }
        }
        printf("\n");
    }
    return 0;
}

