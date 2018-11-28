#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef long double ld;

#define rep(i,a,b) for(ll i=a;i<=b;++i)
#define rev(i,a,b) for(ll i=a;i>=b;i--)
#define pll pair<ll,ll>
#define vll vector<ll>
#define sll set<ll>
#define vpll vector<pll>
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define ln length()
#define M 1000000007
ll t,n,q,dis[101][101];
pll p[103];
ld dp[104];

int main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    ifstream fin;fin.open("C-small-attempt0 (1).in");
    ofstream fout;fout.open("outCSAMLL.txt");

    fout.precision(15);
    fin>>t;
    rep(tt,1,t){

        fin>>n>>q;
        rep(i,1,n) fin>>p[i].F>>p[i].S;
        rep(i,1,n) rep(j,1,n) fin>>dis[i][j];
        ll u,v;fin>>u>>v;

        dp[1]=0.0;
        rep(i,2,n){
            ll tot=0;
            dp[i]=1e18;
            rev(j,i-1,1){
                tot+=dis[j][j+1];
                if(tot<=p[j].F){
                   dp[i]=min(dp[i],(ld)tot/(ld)p[j].S + dp[j]);
                }
            }

        }

        fout<<"Case #"<<tt<<": "<<dp[n]<<'\n';
    }
}
