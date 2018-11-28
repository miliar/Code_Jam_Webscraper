///==================================================///
///                HELLO WORLD !!                    ///
///                  IT'S ME                         ///
///               BISHAL GAUTAM                      ///
///         [ bsal.gautam16@gmail.com ]              ///
///==================================================///
#include<bits/stdc++.h>
#define PI acos(-1.0)
#define X first
#define Y second
#define mpp make_pair
#define nl printf("\n")
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define SZ(x) (int)(x.size())
#define pb(x) push_back(x)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,int>
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

#define _cin ios_base::sync_with_stdio(0),cin.tie(0)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
///int month[]={-1,31,28,31,30,31,30,31,31,30,31,30,31}; //Not Leap Year
///int dx[]= {1,0,-1,0};int dy[]= {0,1,0,-1}; //4 Direction
///int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 Direction
///int dx[]= {2,1,-1,-2,-2,-1,1,2};int dy[]= {1,2,2,1,-1,-2,-2,-1}; //Knight Direction
///==========CONSTANTS=============///
///  Digit     0123456789012345678 ///
#define MX     1002
#define inf    1000000000010000.0
#define MD     1000000007
#define eps    1e-9
///===============================///

int n,k,kk;
double dp[MX+2][MX+2],r,h;
double rr[MX+2],hh[MX+2];
double rrr[MX+2],hhh[MX+2];
int vis[MX+2][MX+2];
vector<pdd>v;

double go(int p,int c) {
    //cout<<p<< " : "<<c<<endl;
    if( c>k || ( n-p )<(k-c) ) return -inf;
    if( c==k ) return rr[p]*rr[p];
    if( vis[p][c]==kk ) return dp[p][c];
    vis[ p ][ c ]=kk;
    double &ret=dp[p][c];
    ret=-inf;
    for(int i=p+1; i<n; i++) {
        ret=max(ret, ( rr[p]*rr[p]-rr[i]*rr[i] )+(2.0*rr[i]*hh[i])+go( i,c+1 )  );
    }
    return ret;
}


int main() {
    int i,j,tc,cs=1;
    freopen("A-large.in", "r", stdin);
    freopen("A-Large_9.txt", "w", stdout);
    kk=1;
    S(tc);
    while( tc-- ) {
        S(n);
        S(k);
        v.clear();
        for(i=0; i<n; i++) {
            scanf("%lf%lf",&r,&h);
            rrr[i]=r,hhh[i]=h;
            double dd=PI*r*r+2.0*PI*r*h;
            //cout<<dd<<endl;
            v.pb( mpp( -r, i ) );
        }
        sort( all(v) );
        for(i=0; i<n; i++) {
            rr[i]=rrr[ v[ i ].Y ];
            hh[i]=hhh[ v[ i ].Y ];
        }
        //CLR(vis);
        double sm=-inf;
        for(i=0;i<n;i++){
            sm=max(sm, 2.0*rr[i]*hh[i]+go(i,1) );
        }
        printf("Case #%d: %.12lf\n",kk++,PI*sm);
        //kk++;
    }
    return 0;
}
