#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

int n,p,a[111];
int c[5];
int dp[5][111][111][111];

int f(int p, int v1, int v2, int v3){
    if(v1<0 || v2<0 || v3<0) return -1;
    if (dp[p][v1][v2][v3]!=-1) return dp[p][v1][v2][v3];
    int &res = dp[p][v1][v2][v3];
    res = (v1+v2+v3>0);
    if(p==2){
        res=max(res,f(p,v1-2,v2,v3)+1);
    }else if(p==3){
        for(int x=0; x<=3; ++x)
            for(int y=0; y<=3; ++y)
                if(x+y>0 && (x+2*y)%3==0)
                    res=max(res,f(p,v1-x,v2-y,v3)+1);
    }else{
        for(int x=0; x<=4; ++x)
            for(int y=0; y<=4; ++y)
                for(int z=0; z<=4; ++z)
                    if(x+y+z>0 && (x+2*y+3*z)%4==0)
                        res=max(res,f(p,v1-x,v2-y,v3-z)+1);
    }
    return res;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    reset(dp,-1);
    int T;
    cin>>T;
    for(int tt=1; tt<=T; ++tt){
        cin>>n>>p;
        reset(c,0);
        for(int i=1; i<=n; ++i){
            cin>>a[i];
            a[i]%=p;
            ++c[a[i]];
        }
        int res = c[0] + f(p,c[1],c[2],c[3]);
        printf("Case #%d: %d\n",tt,res);
    }
}

