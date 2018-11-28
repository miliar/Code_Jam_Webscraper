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
    rep(t,1,T+1){
        ll n,k;
        cin>>n>>k;
        map<ll,ll> m;
        m[-n] = 1;
        cout<<"Case #"<<t<<": ";
        while(k){
            ll a = -m.begin()->X;
            ll b =  m.begin()->Y;
            ll c =(a-1)/2;
            if(k<=b){
                cout<<a-1-c<<" "<<c<<endl;
                break;
            }
            k -= b;
            m[-c]       += b;
            m[-(a-1-c)] += b;
            m.erase(m.begin());
        }
    }
    return 0;
}
