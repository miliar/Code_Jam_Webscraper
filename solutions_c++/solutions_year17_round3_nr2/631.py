#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cassert>
#include <queue>

using namespace std;
#define rep(i,a,n) for (int i=a;i<n;i++)
#define per(i,a,n) for (int i=n-1;i>=a;i--)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define ft first
#define sd second
#define SZ(x) ((int)(x).size())
typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PII;
typedef queue<int> QI;

const LL mod=1000000007;
LL powmod(LL a,LL b) {LL res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
// head

int f[1233][1233][2];
bool a[2333],b[2333];

int ac,aj;

int dp(int x,int y,int z){
    //printf("%d %d %d\n",x,y,z);
    if(f[x][y][z] != -1)return f[x][y][z];
    int re1=23333333,re2=23333333;
    if(z==0){
        if(a[x+y-2] && x>1)re1 = dp(x-1,y,0);
        if(b[x+y-2] && y>0)re2 = dp(x-1,y,1) + 1;
    }else{
        if(a[x+y-2] && x>0)re1 = dp(x,y-1,0) + 1;
        if(b[x+y-2] && y>1)re2 = dp(x,y-1,1);
    }
    f[x][y][z] = min(re1,re2);
    return min(re1,re2);
}


int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T,cas = 1;scanf("%d",&T);
while(T--){
    cin>>ac>>aj;
    memset(a,true,sizeof(a));
    memset(b,true,sizeof(b));
    rep(i,0,1000)rep(j,0,1000)f[i][j][0] = f[i][j][1] = -1;
    rep(i,0,ac){
        int x,y;cin>>x>>y;rep(j,x,y)a[j] = false;
    }
    rep(i,0,aj){
        int x,y;cin>>x>>y;rep(j,x,y)b[j] = false;
    }
    int ans = 23333333;
    if(a[0])f[1][0][0] = 0;
    if(b[0])f[0][1][1] = 1;
    if(a[1439])ans = dp(720,720,0);

    rep(i,0,1000)rep(j,0,1000)f[i][j][0] = f[i][j][1] = -1;

    if(b[0])f[0][1][1] = 0;
    if(a[0])f[1][0][0] = 1;
    if(b[1439])ans = min(ans, dp(720,720,1));

    cout<<"Case #"<<cas++<<": "<<ans<<endl;
}
	return 0;
}
