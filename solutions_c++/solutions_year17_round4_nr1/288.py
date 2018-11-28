//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<fstream>
#include<numeric>
#include<iomanip>
#include<bitset>
#include<list>
#include<stdexcept>
#include<functional>
#include<utility>
#include<ctime>
#include<cassert>
using namespace std;
#define RI(X) scanf("%d", &(X))
#define DRI(X) int (X); scanf("%d", &X)
#define rep(i,a,n) for(int i=(a);i<(int)(n);i++)
#define repd(i,a,b) for(int i=(a);i>=(b);i--)
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define MP make_pair
#define PB push_back
#define AA first
#define BB second
#define OP begin()
#define ED end()
#define SZ size()
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)
const LL MOD = 1000000007;
const double PI = acos(-1.);
const double eps = 1e-9;
LL modPow(LL a,LL b,LL MOD){
    LL ret=1;for(;b;b>>=1){
        if(b&1)ret=ret*a%MOD;a=a*a%MOD;
    }return ret;
}

const int MXN = 100005;
int dp[101][101][101][4];
int G[101],P,N;

void update(int &tp,int w){
    cmax(tp,w);
}

int solve(int a,int b,int c,int x){
    x%=P;
    int &tp=dp[a][b][c][x];
    if(~tp)return tp;
    if(a==0&&b==0&&c==0)return 0;
    int d=0;
    if(!x)d++;
    if(a)update(tp,solve(a-1,b,c,x+1)+d);
    if(b)update(tp,solve(a,b-1,c,x+2)+d);
    if(c)update(tp,solve(a,b,c-1,x+3)+d);
    //cout<<a<<" "<<b<<" "<<c<<" "<<x<<" "<<tp<<"\n";
    return tp;
}
void solve(){
    RI(N);
    RI(P);
    rep(i,0,N)RI(G[i]);
    int a[5];
    memset(a,0,sizeof a);
    int ans = 0;
    rep(i,0,N){
        G[i]%=P;
        if(G[i])a[G[i]-1]++;
        else ans+=1;
    }
    memset(dp,-1,sizeof dp);
    ans += solve(a[0],a[1],a[2],0);
    printf("%d\n",ans);
}

int main(){
    int _T=1;
    scanf("%d",&_T);
    rep(CA,0,_T){
        printf("Case #%d: ",CA+1);
        solve();
    }
    return 0;
}