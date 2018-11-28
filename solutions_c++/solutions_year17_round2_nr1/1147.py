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
ll t,d,n;
pll p[10005];

int main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    ifstream fin;fin.open("A-large (2).in");
    ofstream fout;fout.open("outlarge.txt");

    fout.precision(15);
    fin>>t;
    rep(tt,1,t){

        fin>>d>>n;

        ld ans=1e18;
        while(n--){
            ll x,v;fin>>x>>v;
            ans=min(ans,((ld)d*v)/((ld)d-x));
        }

        fout<<"Case #"<<tt<<": "<<ans<<'\n';



    }
}
