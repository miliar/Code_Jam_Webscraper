#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(a);i<=(b);i++)
#define ll long long
#define pll pair<ll, ll>
#define pii pair<int,int>
#define pb push_back
#define F first
#define S second
#define mod 1000000007
#define maxn 100005
#define boost ios::sync_with_stdio(false);cin.tie(0)
#define fr freopen("source.txt","r",stdin),freopen("output.txt","w",stdout)
#define SET(a,b) memset(a,b,sizeof(a))

ll r[1005],h[1005];

int main(){
    boost;
    
    int tc;
    cin>>tc;
    rep(tct,1,tc){
        cout<<"Case #"<<tct<<": ";
        ll n,k;
        cin>>n>>k;
        rep(i,1,n)cin>>r[i]>>h[i];
        ll tot=0;
        rep(i,1,n){
            ll cur=r[i]*r[i]+2*r[i]*h[i];
            vector<ll> v;
            rep(j,1,n){
                if(j==i)continue;
                if(r[j]>r[i])continue;
                v.pb(2ll*r[j]*h[j]);
            }
            sort(v.begin(), v.end());
            reverse(v.begin(), v.end());
            if(v.size()<k-1)continue;
            rep(j,0,k-2){
                cur+=v[j];
            }
            tot=max(tot,cur);
        }

        cout<<fixed<<setprecision(7)<<(long double)tot*acos(-1)<<endl;
    }

    return 0;
}