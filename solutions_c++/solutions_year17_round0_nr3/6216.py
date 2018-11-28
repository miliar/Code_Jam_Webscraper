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
ll t,n,k;
pll ans[1000001];

bool cmp(pll a,pll b){
    if(a.S!=b.S) return a.S > b.S;
    return a.F > b.F;
}

int main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    ifstream fin;fin.open("C-small-2-attempt0.in");
    ofstream fout;fout.open("outfinal.txt");


    fin>>t;
    rep(tt,1,t){

        fin>>n>>k;
        if(n%2) ans[1]=mp((n-1)/2,(n-1)/2);
        else ans[1]=mp(n/2,n/2-1);

        vpll cur;cur.pb(ans[1]);
        ll ind = 2;

        while(ind<=n){
            vpll tem;
            for(pll xp:cur){
                ll n=xp.F;
                if(n%2) tem.pb(mp((n-1)/2,(n-1)/2));
                else tem.pb(mp(n/2,n/2-1));

                n=xp.S;
                if(n%2) tem.pb(mp((n-1)/2,(n-1)/2));
                else tem.pb(mp(n/2,n/2-1));
            }
            sort(tem.begin(),tem.end(),cmp);

            if(ind -1 + tem.size() >= n)  {
                rep(i,ind,n) ans[i]=tem[i-ind];
                break;
            }
            rep(i,ind,ind-1+tem.size()) ans[i]=tem[i-ind];
            cur=tem;
            ind = ind + tem.size();
        }

        fout<<"Case #"<<tt<<": "<<ans[k].F<<" "<<ans[k].S<<'\n';



    }
}
