#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=(a);i<=(b);i++)
#define ld long double
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

ld p[51],pre[51];

int main(){
    boost;
    
    int t;
    cin>>t;
    rep(tc,1,t){
        SET(pre,0.0);
        cout<<"Case #"<<tc<<": ";
        int n,k;
        ld u,ans=1.0;
        cin>>n>>k>>u;
        rep(i,1,n)cin>>p[i];

        sort(p+1,p+1+n);

        rep(i,1,n)pre[i]=pre[i-1]+1.0*(i-1)*(p[i]-p[i-1]);

        int id=1;
        rep(i,1,n)if(pre[i]<=u)id=i;

        ld div=1.0*(u-pre[id])/id;
        p[id]+=div;

        rep(i,1,id)ans=1.0*ans*p[id];

        rep(i,id+1,n)ans=1.0*ans*p[i];

        cout<<fixed<<setprecision(7)<<ans<<endl;
    }

    return 0;
}