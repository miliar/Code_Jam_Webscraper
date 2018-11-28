#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF=1e18+7;
ll power (ll a,ll e,ll mod)
{
    if (e == 0)
        return 1ll;
    if (e == 1)
        return a % mod;
    if (e & 1)
        return ((a%mod) * power(a,e-1,mod))%mod;
    else
    {
        ll tmp = power(a,e/2,mod);
        return (tmp*tmp)%mod;
    }
}

ll dp[69][3][69];
int num[69];
int k;

ll Calc(int id=0,int flg=1,int lst=0)
{
    if(id == k)
        return 0;
    ll &ret = dp[id][flg][lst];
    if(ret != -1)
        return ret;

    ret = -INF;

    int en = 9;
    if(flg)
        en = num[id];

    for(int i=lst;i<=en;++i)
        ret = max(ret,1ll*i*power(10,k-id-1,1e18+5)+Calc(id+1,flg&&(i==en),i));

    return ret;
}
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for(int j=1;j<=t;j++){
    ll n;
    cin>>n;
    k=0;
    while(n)
    {
        num[k++] = n%10,n/=10;
    }
    for(int i=0;i<k/2;++i)
        swap(num[i],num[k-i-1]);
    memset(dp,-1,sizeof dp);
    cout<<"Case #"<<j<<": "<<Calc()<<endl;

    }
    return 0;
}


