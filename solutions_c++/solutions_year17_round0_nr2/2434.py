#include<bits/stdc++.h>
using namespace std;
/*------- Constants---- */

#define Long                    long long
#define Ulong                   unsigned long long
#define FOR(I,A,B)              for(int I = (A); I < (B) ; ++ I)
#define REP(i,n)                for( int i=0 ; i < n ; i++ )
#define mp                      make_pair
#define pb                      push_back
#define all(x)                  (x).begin(),(x).end()
#define PI                      acos(-1.0)
#define EPS                     1e-9
#define F                       first
#define S                       second
#define lc                      ((n)<<1)
#define rc                      ((n)<<1|1)
#define db(x)                   cout << #x << " -> " << x << endl;
#define Di(x)                   int x;scanf("%d",&x)
#define in(x)                   input(x)
#define in2(x,y)                input(x), input(y)
#define in3(x,y,z)              input(x), input(y),input(z)
#define ins(x)                  scanf("%s",x)
#define ind(x)                  scanf("%lf",&x)
#define ms(ara_name,value)      memset(ara_name,value,sizeof(ara_name))
#define IO                      ios_base::sync_with_stdio(0);cin.tie(0)
#define READ                    freopen("/Users/matrixcode/Desktop/in.txt","r",stdin)
#define WRITE                   freopen("/Users/matrixcode/Desktop/out.txt","w",stdout)

template<class T > void input(T &x){
    char c = getchar();x = 0;
    for(;(c<48 || c>57);c = getchar());
    for(;c>47 && c<58;c = getchar()) {x = (x<<1) + (x<<3) + c - 48;}
}
inline long long bigmod(long long p,long long e,long long M){
    long long ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}

/***************************** END OF TEMPLATE *******************************/

const int N = 1001;
string y;
long long POW[20];
long long dp[20][10][2];

long long F(int idx,int prev, bool f )
{
    if(idx < 0) return 0;
    if(dp[idx][prev][f] !=-1) return dp[idx][prev][f];
    long long ret = -1e18;
    for(int i= prev;i<10;i++){
        if(f && y[idx]-'0' <i) continue;
        long long now =i*POW[idx] + F(idx-1, i , f && (i == y[idx]-'0'));
        ret = max(ret,  now);
        
    }
    return dp[idx][prev][f] = ret;
    
}

int main()
{
    READ;
    WRITE;
    POW[0]=1;
    for(int i=1;i<20;i++) POW[i] = 10*POW[i-1];
    Di(t);
    int cs=0;
    while(t--){
        long long n;
        cin>> n;
        y=to_string(n);
        reverse(all(y));
        memset(dp,-1,sizeof dp);
        printf("Case #%d: %lld\n",++cs, F((int)y.size()-1,0, 1));
    }
    return 0;
}
