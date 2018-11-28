#include<bits/stdc++.h>
using namespace std;
/*------- Constants---- */

#define Long                    long long
#define Ulong                   unsigned long long
#define FOR(I,A,B)              for(long long I = (A); I < (B) ; ++ I)
#define REP(i,n)                for( long long i=0 ; i < n ; i++ )
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
#define Di(x)                   long long x;scanf("%d",&x)
#define in(x)                   input(x)
#define in2(x,y)                input(x), input(y)
#define in3(x,y,z)              input(x), input(y),input(z)
#define ins(x)                  scanf("%s",x)
#define ind(x)                  scanf("%lf",&x)
#define ms(ara_name,value)      memset(ara_name,value,sizeof(ara_name))
#define IO                      ios_base::sync_with_stdio(0);cin.tie(0)
#define READ                    freopen("in.txt","r",stdin)
#define WRITE                   freopen("out2.txt","w",stdout)

template<class T > void input(T &x)
{
    char c = getchar();
    x = 0;
    for(; (c<48 || c>57); c = getchar());
    for(; c>47 && c<58; c = getchar()) {
        x = (x<<1) + (x<<3) + c - 48;
    }
}
inline long long bigmod(long long p,long long e,long long M)
{
    long long ret = 1;
    for(; e > 0; e >>= 1) {
        if(e & 1) {
            ret = (ret * p) % M;
        }
        p = (p * p) % M;
    }
    return ret;
}
template <class T> inline T gcd(T a,T b)
{
    if(b==0) {
        return a;
    }
    return gcd(b,a%b);
}
template <class T> inline T modinverse(T a,T M)
{
    return bigmod(a,M-2,M);
}

/***************************** END OF TEMPLATE *******************************/

const int N = 101;
int cnt[5];
int g[N];
int p,n;
char dp[3][N][N][N][N][4];

int solve(int p,int a,int b,int c,int d,int rm)
{
    int t = a+b+c+d;
    if(dp[p-2][a][b][c][d][rm] != -1) {
        return dp[p-2][a][b][c][d][rm];
    }
    if(t==0) {
        return 0;
    }
    int r = 0;
    if(a) {
        r = max(r, solve(p,a-1,b,c,d,rm ));
    }
    if(b) {
        r = max(r, solve(p,a,b-1,c,d,(rm+1)%p));
    }
    if(c) {
        r = max(r, solve(p,a,b,c-1,d,(rm+2)%p));
    }
    if(d) {
        r = max(r, solve(p,a,b,c,d-1,(rm+3)%p));
    }
    if(rm == 0) {
        r++;
    }
    return dp[p-2][a][b][c][d][rm]=r;
}
int main()
{
    memset(dp,-1,sizeof dp);
    for(int i=0;i<3;i++) solve(i+2,100,100,100,100,0);

    READ;
    WRITE;

    int t,cs=0;
    in(t);
    while(t--) {
        in2(n,p);
        memset(cnt,0,sizeof cnt);
        for(int i=0; i<n; i++) {
            in(g[i]);
            cnt[g[i]%p] ++;
        }
        printf("Case #%d: %d\n",++cs, solve(p,cnt[0],cnt[1],cnt[2],cnt[3],0));
    }
}
