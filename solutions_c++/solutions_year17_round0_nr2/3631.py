#include"iostream"
#include"cstring"
#include"cstdio"
#include"queue"
#include"set"
#include"map"
#include"algorithm"
#include"cmath"
#define clr(a) memset(a,0,sizeof(a))
#define mdzz int mid=(L+R)>>1;
#define ls pos<<1
#define rs pos<<1|1
#define lson L,mid,ls
#define rson mid+1,R,rs
#define fr first
#define sc second
using namespace std;

typedef long long LL;

const int N = 20;
const int M = 2e6+5;
const int INF = 0x3f3f3f3f;

int cas=1,T;

LL dp[N][11];
int dig[N];

LL dfs(int pos,int pre,int first,int limit){
    if(!pos) return !first;
    LL &ans = dp[pos][pre];
    if(!limit && !first && ans!=-1) return ans;
    int end = limit? dig[pos] : 9;
    LL cnt=0;
    for(int i=pre;i<=end;i++){
        cnt+=dfs(pos-1,i,first&&!i,limit&&i==end);
    }
    if(!limit &&!first) ans=cnt;
    return cnt;
}

LL solve(LL x){
    int cnt=0;
    while(x){
        dig[++cnt]=x%10;
        x/=10;
    }
    return dfs(cnt,0,1,1);
}

LL n;

int main(){
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
    for(scanf("%d",&T);T;T--){
        memset(dp,-1,sizeof(dp));
        scanf("%lld",&n);
        LL k=solve(n);
        //cout<<k<<endl;
        LL low=1,high=n,mid,ans;
        while(low<=high){
            mid=(low+high)>>1;
            if(solve(mid)>=k) ans=mid,high=mid-1;
            else low=mid+1;
        }

        printf("Case #%d: %lld\n",cas++,ans);
    }
    return 0;
}
/*
4
132
1000
7
111111111111111110
*/
