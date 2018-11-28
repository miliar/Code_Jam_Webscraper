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
#define MX     52
#define inf    2000000010
#define MD     1000000007
#define eps    1e-9
///===============================///

char s[22];
ll dp[20][2][10];
int n;
ll go(int p,int ch,int m){
    if( p==n ) return 1;
    ll &ret=dp[ p ][ ch ][ m ];
    if( ret!=-1 ) return ret;
    ret=0;
    int mx=s[ p ]-'0';
    if(ch)mx=9;
    for(int i=mx;i>=max(0,m);i--){
        ret=(ret||go( p+1,ch||i<mx,i ));
    }
    return ret;
}

string str;
ll po(int p,int ch,int m){
    if( p==n ) return 1;
    ll &ret=dp[ p ][ ch ][ m ];
    int mx=s[ p ]-'0';
    if(ch)mx=9;
    for(int i=mx;i>=max(0,m);i--){
        if( ret==go( p+1,ch||i<mx,i ) ){
            str+=(char)(i+'0');
            po( p+1,ch||i<mx,i );
            break;
        }
    }
    return ret;
}

int main() {
    freopen("B-large.in","r",stdin);
    freopen("Output_B_Large.txt","w",stdout);
    int tc,cs=1,i,j,k;
    ll nm;
    S(tc);
    while(tc--) {
        SL(nm);
        sprintf(s,"%lld",nm);
        n=strlen(s);
        SET(dp);
        ll res=go( 0,0,0 );
        str="";
        po( 0,0,0 );
        int nz=0;
        n=SZ(str);
        string ans="";
        for(i=0;i<n;i++){
            if( str[i]!='0' ){
                nz=1;
            }
            if(nz)ans+=str[ i ];
        }
        printf("Case #%d: %s\n",cs++,ans.c_str());
    }
    return 0;
}
