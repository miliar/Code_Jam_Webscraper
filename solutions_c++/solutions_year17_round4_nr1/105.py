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
        int n,p;
        cin>>n>>p;
        vi v(p,0);
        rep(i,0,n){
            int x;
            cin>>x;
            v[x%p] ++;
        }
        int ans = v[0];
        if(p==2){
            ans += (v[1]+1)/2;
        }
        if(p==3){
            int k = min(v[1],v[2]);
            ans += k;
            v[1] -= k;
            v[2] -= k;
            ans += (v[1]+2)/3;
            ans += (v[2]+2)/3;
        }
        if(p==4){
            int k = min(v[1],v[3]);
            ans += k;
            v[1] -= k;
            v[3] -= k;
            k = v[2]/2;
            ans += k;
            v[2] -= k*2;
            if(v[2] == 1 && v[1]) v[1]+=2;
            if(v[2] == 1 && v[3]) v[3]+=2;
            ans += (v[1]+3)/4;
            ans += (v[2]+3)/4;
        }
        cout<<"Case #"<<tt<<": "<<ans<<"\n";
    }
    return 0;
}
