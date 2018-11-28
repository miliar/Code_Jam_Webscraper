

#include <bits/stdc++.h>
using namespace std;

const int mxn = 11;
typedef long long ll;
const int mx = 2e5+50;
const ll INF = 1e18+7;

ll power (ll a,ll x,ll mod)
{
    if (x == 0)  return 1ll;
    ll r=power(a,x/2,mod);
    r=(r*r)%mod;
    if(x&1)return (r*a)%mod;
    return r;
}
int N[25];
ll dp[25][4][15],n;
int k;

ll sol(int id=0,int flg=1,int lst=0)
{
    if(id == k)  return 0;
    ll &ans = dp[id][flg][lst];
    if(ans != -1)return ans;
    ans = -INF;
    int H = 9;
    if(flg)  H = N[id];
    for(int i=lst;i<=H;++i){
        ll kk=1ll*i*power(10,k-id-1,INF)+sol(id+1,flg&&(i==H),i);
        ans = max(ans,kk);
    }
    return ans;
}


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("outA.txt","w",stdout);
    int t;cin>>t;
    for(int cs=1;cs<=t;cs++){
    cin>>n;
    k=0;
    memset(dp,-1,sizeof dp);
    memset(N,0,sizeof N);
    while(n)   N[k++] = n%10,n/=10;
    for(int i=0;i<k/2;++i)   swap(N[i],N[k-i-1]);
    cout<<"Case #"<<cs<<": "<<sol()<<endl;
    }
    return 0;
}


