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
int T;
LL n;
int f[20];
int ans[20];
int main(){
    int cas = 0;
freopen("B-large.in","r",stdin);
freopen("B.out","w",stdout);
scanf("%d",&T);while(T--){cas++;
    memset(f,0,sizeof(f));
    rep(i,0,20)ans[i] = 233;
    cin>>n;int now = 0;
    while(n){
        f[now++] = n%10;
        n/=10;
    }
    rep(i,0,now){
        bool flag = false;
        rep(j,0,i)if(f[j]<f[i])flag=true;
        if(flag){
            f[i]--;
            rep(j,0,i)f[j] = 9;
        }
    }
    if(f[now-1]==0)f[now-1]=-1;
    per(i,0,now-1)if(f[i]==0 && f[i+1]==-1)f[i] = -1;
    cout<<"Case #"<<cas<<": ";
    per(i,0,now)if(f[i]!=-1)cout<<f[i];
    cout<<endl;
}
    fclose(stdin);
    fclose(stdout);
	return 0;
}
