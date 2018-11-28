#include <bits/stdc++.h>
using namespace std;
#define rep(it,st,en) for(int it=(st);it<(int)(en);++it)
#define allof(c) (c).begin(), (c).end()
#define mt make_tuple
#define mp make_pair
#define pb push_back
#define X first
#define Y second
typedef long long int ll; 
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<ll,ll> pii;
const int INF=(int)1e9; 
const double EPS=(ld)1e-7;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    rep(t,1,T+1){
        int n,p;
        cin>>n>>p;
        vector<ll> r(n);
        rep(i,0,n){
            cin>>r[i];
        }
        multiset<pii> event;
        rep(i,0,n){
            rep(j,0,p){
                ll x;
                cin>>x;
                ll k1 = 100*x/(110*r[i]);
                ll k2 = 100*x/(90*r[i]);
                while(k1*110*r[i] < 100*x) k1++;
                while(k2*90*r[i]  <= 100*x) k2++;
                event.insert({k1,i});
                event.insert({k2,i-n});
            }
        }
        int q = 0,ans=0;
        vi alive(n,0);
        vi killed(n,0);
        for(auto e:event){
            int s = e.Y;
            if(s<0){
                s+=n;
                if(killed[s]) killed[s]--;
                else {
                    alive[s]--;
                    if(alive[s] == 0) q--;
                }
            }
            else{
                alive[s]++;
                if(alive[s] == 1) q++;
            }
            if(q == n){
                rep(i,0,n){
                    alive[i]--;
                    killed[i]++;
                    if(alive[i] == 0) q--;
                }
                ans++;
            }
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
