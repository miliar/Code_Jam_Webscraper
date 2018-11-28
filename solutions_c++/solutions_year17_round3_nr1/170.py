#include<bits/stdc++.h>

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define FRI freopen("A-large.in","r",stdin)
#define FRO freopen("A-large.out","w",stdout)
#define debug(args...) {dbg,args; cerr<<endl;}
#define DB(x) #x"=>",x
#define RAD(x) ((x*PI)/180)
#define NEX(x) ((x)==n-1?0:(x)+1)
#define PRE(x) ((x)==0?n-1:(x)-1)
#define DEG(x) ((x*180)/PI)

#define EPS 1e-6
#define INF 1000000007
#define MOD 1000000007
#define MAXN 1005
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const double PI=acos(-1.0);

struct debugger{
    template<typename T> debugger& operator , (const T& v){
        cerr<<v<<" ";
        return *this;
    }
}dbg;

pair<LD,LD>pancakes[MAXN];
LD dp[MAXN][MAXN];

void solve(int cas) {
    int i,j,n,k;
    scanf("%d %d",&n,&k);
    for(i=0;i<n;i++) {
        cin>>pancakes[i].F>>pancakes[i].S;
    }
    sort(pancakes,pancakes+n);
    reverse(pancakes,pancakes+n);
    for(i=0;i<n;i++) {
        dp[i][0]=PI*pancakes[i].F*(pancakes[i].F+2*pancakes[i].S);
        if(i>0) {
            dp[i][0]=max(dp[i][0],dp[i-1][0]);
        }
        for(j=1;j<=min(k-1,i);j++) {
            dp[i][j]=dp[i-1][j-1]+2*PI*pancakes[i].F*pancakes[i].S;
            if(j<i) {
                dp[i][j]=max(dp[i][j],dp[i-1][j]);
            }
        }
    }
    cout<<"Case #"<<cas<<": "<<setprecision(9)<<fixed<<dp[n-1][k-1]<<endl;
}

int main() {
    FRI;
    FRO;
    int T,t=0;
    scanf("%d",&T);
    while(t++<T) {
        solve(t);
    }
    return 0;
}
