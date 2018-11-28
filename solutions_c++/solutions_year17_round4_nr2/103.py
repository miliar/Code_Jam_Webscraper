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
typedef pair<int,int> pii;
const int INF=(int)1e9; 
const double EPS=(ld)1e-7;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin>>T;
    rep(tt,1,T+1){
        int n,c,m;
        cin>>n>>c>>m;
        vi v(n,0);
        vi t(c,0);
        rep(i,0,m){
            int p,b;
            cin>>p>>b;
            v[p-1]++;
            t[b-1]++;
        }
        int d = 0;
        rep(i,0,c) d = max(d,t[i]);
        int acc = 0;
        rep(i,0,n){
            acc += v[i];
            int k = (acc+i)/(i+1);
            d = max(d,k);
        }
        int prom = 0;
        rep(i,0,n){
            prom += max(0,v[i]-d);
        }
        cout<<"Case #"<<tt<<": "<<d<<" "<<prom<<endl;
    }
    return 0;
}
