///==================================================///
///                HELLO WORLD !!                    ///
///                  IT'S ME                         ///
///               BISHAL GAUTAM                      ///
///         [ bsal.gautam16@gmail.com ]              ///
///==================================================///
#include<bits/stdc++.h>
#define X first
#define Y second
#define mpp make_pair
#define nl printf("\n")
#define SZ(x) (int)(x.size())
#define pb(x) push_back(x)
#define pii pair<int,int>
#define pll pair<ll,ll>
///---------------------
#define S(a) scanf("%d",&a)
#define P(a) printf("%d",a)
#define SL(a) scanf("%lld",&a)
#define S2(a,b) scanf("%d%d",&a,&b)
#define SL2(a,b) scanf("%lld%lld",&a,&b)
///------------------------------------
#define all(v) v.begin(),v.end()
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define fr(i,a,n) for(int i=a;i<=n;i++)
using namespace std;
typedef long long ll;

///  Digit     0123456789012345678 ///
#define MX     2005
#define inf    2000000010
#define MD     1000000007
#define eps    1e-9
///===============================///

char s[MX+2];
ll n,nn,k;
//
//struct data {
//    ll ls,rs,id,Mn,Mx;
//    data() {};
//    data(ll a,ll b,ll c) {
//        ls=a,rs=b,id=c;
//        Mx=max(a,b);
//        Mn=min(a,b);
//    }
//    bool friend operator<(data A,data B) {
//        if( A.Mn==B.Mn ) {
//            if( A.Mx==B.Mx ) {
//                return A.id>B.id; ///LeftMost
//            } else return A.Mx<B.Mx;
//        } else return A.Mn<B.Mx; ///Ulta
//    }
//};

map<ll,ll>Mp;
int main() {
    freopen("C-large.in","r",stdin);
    freopen("Output_C_Large.txt","w",stdout);
    int tc,cs=1,i,j;
    ll md,ls,rs,id;
    S(tc);
    while( tc-- ) {
        SL2(n,k);
        Mp.clear();

        priority_queue< ll >PQ;

        ///data: Ls,Rs,Index
        PQ.push( n+1 );

        Mp[ n+1 ]=1;
        while( true ) {

            ll tp=PQ.top();
            PQ.pop();

            ll tot=Mp[ tp ];
            Mp[ tp ]=0;

            ll lft=(tp/2LL);
            ll rgt=(tp+1)/2LL;

            k-=tot;

            if( k<=0 ) {
                printf("Case #%d: %lld %lld\n",cs++,rgt-1,lft-1 );
                break;
            }

            if( !Mp.count( lft ) ) PQ.push( lft );
            if( !Mp.count( rgt ) ) PQ.push( rgt );

            Mp[  lft ]+=tot;
            Mp[  rgt ]+=tot;

        }
    }
    return 0;
}
